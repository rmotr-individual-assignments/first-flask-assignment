from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World"

@app.route('/python')
def python():
    html = """
        <html>
                {python_h1}
        </html>
    """
    python_h1 ="<h1>{title}</h1>".format(title="Python Programming Language")
    
    return html.format(python_h1=python_h1)
