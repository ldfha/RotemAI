from flask import Flask, render_template

app = Flask(__name__);

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hello')
def hello():
    name = "길동아"
    addr = "강남구 테헤란로"
    return render_template("hello.html", name=name, juso=addr)
    # 페이지 소스보기 하면 완성된 문장이 넘겨져있음
    # 서버에서 먼저 렌더링을 하고 html을 return한다.

@app.route('/world')
def world():
    return render_template("world.html")

if __name__ == '__main__':
    app.run(debug=True)
