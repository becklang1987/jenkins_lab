# 使用官方的 Ubuntu 基础镜像
FROM ubuntu:latest

# 设置环境变量，以非交互模式运行
ENV DEBIAN_FRONTEND=noninteractive

# 更新包列表并安装所需软件
RUN apt-get update && \
    apt-get install -y python3 python3-pip vim net-tools curl iputils-ping
RUN mkdir app
# 为应用创建工作目录
WORKDIR /app

# 将当前目录的内容复制到工作目录
COPY *.py .

# 安装 Python 依赖
RUN apt install -y python3-flask

# 暴露应用运行的端口
EXPOSE 5000

# 运行 Flask 应用
CMD ["python3", "123.py"]