from flask import Flask, request, jsonify

import mail

app = Flask(__name__)


@app.route('/workday_webhook/', methods=['POST'])
def workday_webhook():
    try:
        # 获取来自 Workday 的 JSON 数据
        new_employee_data = request.json

        # 输出接收到的新员工数据
        print(f"Received new employee data: {new_employee_data}")

        # 解析必要的信息，例如姓名和邮箱
        employee_name = new_employee_data.get('name')
        employee_email = new_employee_data.get('email')
        # 其他可能需要的字段（根据实际的 Workday webhook 结构决定）

        if not employee_name or not employee_email:
            return jsonify({"error": "Invalid data"}), 400

        # 发送新员工信息到指定邮箱
        mail.send_email(employee_name, employee_email, new_employee_data)

        return jsonify({"status": "success"}), 200

    except Exception as e:
        # 捕获所有异常并打印错误信息
        print(f"Error received: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)  # 设置端口号为 5000，可以根据需要修改