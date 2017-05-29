from flask import Flask

app = Flask(__name__)


@app.route('/python')
def home():
    return <hl>'Python Programming Language'<\hl>
