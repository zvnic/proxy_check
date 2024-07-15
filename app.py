from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def get_ip():
    ip_address = request.remote_addr
    return jsonify({'ip': ip_address})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5086)
