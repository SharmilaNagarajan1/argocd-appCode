from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Payment Service !'

@app.route('/payment')
def payment():
    return 'Payment service is running'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
