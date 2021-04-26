"""练习1：使用浏览器访问服务端代码，得到一个图片展示出来。图片可自行选择
注意：图片格式相应内容格式使用
Content-Type:image/jpeg"""

"""
http请求和响应 演示
"""
from socket import *

#接收http请求，回复响应
def handle(connfd):
    # 接收HTTP请求
    request = connfd.recv(1024)
    #请求内容
    info = request.decode().split(' ')[1]
    if info == "/1":
        filename = "1.jpg"
    elif info == "/2":
        filename = "2.jpg"
    elif info == "/3":
        filename = "3.jpg"
    else:
        filename = "404.jpg"


    # 组织响应
    response = "HTTP/1.1 200 OK\r\n"
    response += "Content-Type:image/jpeg\r\n"
    response += "\r\n"
    with open(filename,'rb') as f:
        data = f.read()
    response = response.encode() + data

    #发送给浏览器
    connfd.send(response)


def main():

    sock = socket()
    sock.bind(("0.0.0.0",8002))
    sock.listen(5)
    while True:
        # 接收浏览器连接请求
        connfd,addr = sock.accept()
        print("Connect from",addr)
        #处理浏览器请求
        handle(connfd)
        connfd.close()
    sock.close()

if __name__ == '__main__':
    main()
