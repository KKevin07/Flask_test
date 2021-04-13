from flask import  Flask,render_template

app = Flask(__name__)
#FLASK_DEBUG=1



@app.route("/")
def hello_world():
    return 'Hello World!'



if __name__ == '__main__':
    app.run()       #web默认运行在本机地址：http://127.0.0.1:5000/















