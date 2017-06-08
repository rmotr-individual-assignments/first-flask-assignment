from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World"

@app.route('/python')
def py_route():
    html = "<html><hl>Python Programming Language</hl></html>"
    return html
