from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Now returns an HTML h1 tag
    return '<h1>Hello World :)</h1>'

@app.route('/greet')
def greet():
    return "Hello"


if __name__ == '__main__':
    app.run()

