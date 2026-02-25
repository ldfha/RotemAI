# 단순한 HTTPServer 구축 - 기본적인 socket 연결 관리
from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 7777

handler = SimpleHTTPRequestHandler  # 문서를 읽어 client로 전송하는 역할

# HTTPSserver 객체 생성
serv = HTTPServer(('127.0.0.1', PORT), handler)
print('웹 서비스 시작...')
serv.serve_forever()    # 웹서비스 무한 루핑