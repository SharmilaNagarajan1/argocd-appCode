from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/payment')
def payment():
    return jsonify(message="Payment Service Working!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
