from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World"

@app.route('/')
def python():
	return "<html><h1>Python Programming Language</h1></html>"
