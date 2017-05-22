from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return hello world

@app.route('/python')
def python():
    return <html><h1> Python Programming Language</h1></html>



