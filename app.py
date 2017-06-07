from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"


@app.route('/python')
def hello_worldzzz():
    return '<html><h1>python programming language</h1></html>'

if __name__ == '__main__':
    app.run()


