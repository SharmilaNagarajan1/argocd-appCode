from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Login Service !!!'

@app.route('/login')
def login():
    return 'Login service is running!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

