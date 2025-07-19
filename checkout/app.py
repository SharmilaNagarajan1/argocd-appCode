from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Checkout Service !'

@app.route('/checkout')
def checkout():
    return 'Checkout Service is running!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
