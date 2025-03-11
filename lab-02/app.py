from flask import Flask, render_template, request, json
from ex01.cipher.caesar.caesar_cipher import CaesarCipher
from ex01.cipher.playfair.playfair_cipher import PlayFairCipher
from ex01.cipher.railfence.railfence_cipher import RailFenceCipher
from ex01.cipher.transposition.transposition_cipher import TranspositionCipher
from ex01.cipher.vigenere.vigenere_cipher import VigenereCipher

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template('caesar.html')
@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text : {text} <br> key : {key} <br> encrypted text : {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text : {text} <br> key : {key} <br> decrypted text : {decrypted_text}"

@app.route("/playfair")
def playfair():
    return render_template('playfair.html')
@app.route("/encryptPlayfair", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    
    Playfair = PlayFairCipher()
    matrix = Playfair.create_playfair_matrix(key)  # Tạo ma trận Playfair
    encrypted_text = Playfair.playfair_encrypt(text, matrix)  # Gọi đúng phương thức
    
    return f"text : {text} <br> key : {key} <br> encrypted text : {encrypted_text}"

@app.route("/decryptPlayfair", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    
    Playfair = PlayFairCipher()
    matrix = Playfair.create_playfair_matrix(key)  # Tạo ma trận Playfair
    decrypted_text = Playfair.playfair_decrypt(text, matrix)  # Gọi đúng phương thức
    
    return f"text : {text} <br> key : {key} <br> decrypted text : {decrypted_text}"


@app.route("/railfence")
def railfence():
    return render_template('railfence.html')
@app.route("/encryptRailfence", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    
    Railfence = RailFenceCipher()
    encrypted_text = Railfence.rail_fence_encrypt(text, key)  # Gọi đúng phương thức
    
    return f"text : {text} <br> key : {key} <br> encrypted text : {encrypted_text}"

@app.route("/decryptRailfence", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    
    Railfence = RailFenceCipher()
    decrypted_text = Railfence.rail_fence_decrypt(text, key)  # Gọi đúng phương thức
    
    return f"text : {text} <br> key : {key} <br> decrypted text : {decrypted_text}"


@app.route("/transposition")
def transposition():
    return render_template('transposition.html')
@app.route("/encryptTransposition", methods=['POST'])
def transposition_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    
    Transposition = TranspositionCipher()
    encrypted_text = Transposition.encrypt(text, key)  # Gọi đúng phương thức
    
    return f"text : {text} <br> key : {key} <br> encrypted text : {encrypted_text}"

@app.route("/decryptTransposition", methods=['POST'])
def transposition_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    
    Transposition = TranspositionCipher()
    decrypted_text = Transposition.decrypt(text, key)  # Gọi đúng phương thức
    
    return f"text : {text} <br> key : {key} <br> decrypted text : {decrypted_text}"


@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')
@app.route("/encryptVigenere", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    
    Vigenere = VigenereCipher()
    encrypted_text = Vigenere.vigenere_encrypt(text, key)  # Gọi đúng phương thức
    
    return f"text : {text} <br> key : {key} <br> encrypted text : {encrypted_text}"

@app.route("/decryptVigenere", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    
    Vigenere = VigenereCipher()
    decrypted_text = Vigenere.vigenere_decrypt(text, key)  # Gọi đúng phương thức
    
    return f"text : {text} <br> key : {key} <br> decrypted text : {decrypted_text}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050, debug=True)