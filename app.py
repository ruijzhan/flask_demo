from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Alibaba"

app.run(host="0.0.0.0")
