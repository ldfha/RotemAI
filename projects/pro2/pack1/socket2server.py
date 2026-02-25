import socket
import sys

# HOST = '127.0.0.1'  # locathost만 가능
HOST = ''   # 누구든 가능
PORT = 7788

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    serversock.bind((HOST, PORT))
    serversock.listen(5)
    print('서버 서비스(무한 루핑) 중 ...')
    while True:
        conn, addr = serversock.accept()
        print('client info : ', addr[0], ' ', addr[1])  # ip 주소, port 번호
        print(conn.recv(1024).decode()) # 수신 메세지 출력
        # 메세지 송신 to client
        conn.send(('from server : ' + str(addr[1]) + '너도 잘지내라.').encode('utf_8'))
except Exception as e:
    print('err : ', e)
    sys.exit()
finally:
    serversock.close()