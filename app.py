from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return'Hello World'

@app.route('/python')
def phython():
    return"""
    <html><hl>Python Programming Language<html><\hl>
    """
