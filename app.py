
from flask import Flask, Response

app = Flask(__name__)



@app.route('/')
def index():
    return "hello"

if __name__ == '__main__':
    app.run(debug=True)
