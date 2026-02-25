# https://velog.io/@rookieand/MIME-type%EC%9D%80-%EB%AD%90%EA%B3%A0-Content-type%EC%9D%80-%EB%AD%94%EB%8D%B0
# https://www.hongreat.co.kr/blog/wordpress/MIME-type-Content-type--%EC%9E%90%EC%A3%BC%EC%93%B0%EB%8A%94-37%EA%B0%80%EC%A7%80-%ED%8C%8C%EC%9D%BC%ED%99%95%EC%9E%A5%EC%9E%90-%ED%99%95%EC%9D%B8%ED%95%98%EA%B8%B0
import sys
sys.stdout.reconfigure(encoding='utf-8')
s1 = "자료1"
s2 = "두번째 자료"

print('Content-Type:text/html;charset=utf-8')

print("""
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>world</title>
</head>
<body>
    <h1>World 페이지</h1> 
    자료출력 {0} {1}     
    <br/>
    <img src="../images/img.jpeg"  width="500px"/>
    <br/>
    <a href="../index.html">메인으로</a>
    <br/>
</body>
      """.format(s1, s2))   # template