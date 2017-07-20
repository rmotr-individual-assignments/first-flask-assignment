from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    pass

@app.route('/python')
def code():
    html_code = "<html><h1>Python Programming Language</h1></html>"
    return html_code
