import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(employee_name, employee_email, employee_data):
    sender_email = "yinzhaji23@163.com"  # 你的 Gmail 地址
    receiver_email = "yinzhaji23@gmail.com"  # 要发送到的邮箱地址
    password = "E23kis!4"  # 你的 Gmail 密码或应用专用密码

    # 配置邮件内容
    subject = f"New Employee: {employee_name}"
    body = f"New employee information:\n\nName: {employee_name}\nEmail: {employee_email}\n\nFull Data: {employee_data}"

    # 创建邮件对象
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # 添加邮件正文
    msg.attach(MIMEText(body, 'plain'))

    try:
        # 连接 Gmail SMTP 服务器并发送邮件
        server = smtplib.SMTP('smtp.163.com')
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")