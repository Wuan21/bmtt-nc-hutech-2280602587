from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.Playfair import PlayFairCipher

app = Flask(__name__)

#caesar cipher algorithm
caesar_cipher = CaesarCipher()
#vigenere cipher algorithm
vigenere_cipher = VigenereCipher()
#railfence cipher algorithm
railfence_cipher = RailFenceCipher()
#playfair cipher algorithm
playfair_cipher = PlayFairCipher()

@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    try:
        data = request.get_json()
        plain_text = data['plain_text']
        key = int(data['key'])
        encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
        return jsonify({'encrypted_text': encrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    try:
        data = request.get_json()
        encrypted_text = data['encrypted_text']
        key = int(data['key'])
        decrypted_text = caesar_cipher.decrypt_text(encrypted_text, key)
        return jsonify({'decrypted_text': decrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    try:
        data = request.get_json()
        plain_text = data['plain_text']
        key = data['key']
        encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
        return jsonify({'encrypted_text': encrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    try:
        data = request.get_json()
        encrypted_text = data['encrypted_text']
        key = data['key']
        decrypted_text = vigenere_cipher.vigenere_decrypt(encrypted_text, key)
        return jsonify({'decrypted_text': decrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    try:
        data = request.get_json()
        plain_text = data['plain_text']
        num_rails = int(data['num_rails'])
        encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, num_rails)
        return jsonify({'encrypted_text': encrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    try:
        data = request.get_json()
        encrypted_text = data['encrypted_text']
        num_rails = int(data['num_rails'])
        decrypted_text = railfence_cipher.rail_fence_decrypt(encrypted_text, num_rails)
        return jsonify({'decrypted_text': decrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 400   

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    try:
        data = request.get_json()
        plain_text = data['plain_text']
        key = data['key']
        matrix = playfair_cipher.create_playfair_matrix(key)
        encrypted_text = playfair_cipher.playfair_encrypt(plain_text, matrix)
        return jsonify({'encrypted_text': encrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    try:
        data = request.get_json()
        encrypted_text = data['encrypted_text']
        key = data['key']
        matrix = playfair_cipher.create_playfair_matrix(key)
        decrypted_text = playfair_cipher.playfair_decrypt(encrypted_text, matrix)
        return jsonify({'decrypted_text': decrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

#main function
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000 ,debug=True)