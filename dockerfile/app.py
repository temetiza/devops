from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, this is my Python app running in a Docker container!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
