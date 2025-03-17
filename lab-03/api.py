import sys
import os
from flask import Flask, request, jsonify

# Thêm đường dẫn tới module 'cipher' và 'ui'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'cipher')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'ui')))

from ecc_cipher import ECCipher

app = Flask(__name__)

ecc_cipher = ECCipher()

@app.route('/api/ecc/generate_keys', methods=['GET'])
def ecc_generate_keys():
    ecc_cipher.generate_keys()
    return jsonify({"message": "Keys generated successfully"})

@app.route('/api/ecc/sign', methods=['POST'])
def ecc_sign_message():
    data = request.json
    message = data['message']
    private_key, _ = ecc_cipher.load_keys()
    signature = ecc_cipher.sign(message, private_key)
    signature_hex = signature.hex()
    return jsonify({"signature": signature_hex})

@app.route('/api/ecc/verify', methods=['POST'])
def ecc_verify_signature():
    data = request.json
    message = data['message']
    signature_hex = data['signature']
    _, vk = ecc_cipher.load_keys()
    signature = bytes.fromhex(signature_hex)
    is_verified = ecc_cipher.verify(message, signature, vk)
    return jsonify({"is_verified": is_verified})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)