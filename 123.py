import requests
import time

def get_response_time(url):
    """
    发送HTTP GET请求并返回响应时间。

    :param url: 请求的URL
    :return: 响应时间（秒）
    """
    try:
        start_time = time.time()
        response = requests.get(url)
        response.raise_for_status()  # 如果响应状态码不是200，抛出HTTPError异常
        end_time = time.time()
        response_time = end_time - start_time
        return response_time
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

if __name__ == "__main__":
    # 目标URL
    url = "http://www.baidu.com"
    
    # 获取响应时间
    response_time = get_response_time(url)
    
    # 打印响应时间
    if response_time is not None:
        print(f'HTTP响应时间: {response_time:.4f} 秒')