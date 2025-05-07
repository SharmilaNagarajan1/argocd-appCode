from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Login Service is running!'

@app.route('/login')
def login():
    return 'Login functinality is here!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

