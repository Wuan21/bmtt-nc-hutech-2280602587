from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad
import socket
import threading
import hashlib

def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext

def decrypt_message(key, encrypted_message):
    iv = encrypted_message[:AES.block_size]
    ciphertext = encrypted_message[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted.decode()

def receive_messages(socket, aes_key):
    while True:
        try:
            message = socket.recv(1024)
            if not message:
                break
            decrypted = decrypt_message(aes_key, message)
            print(f"\nReceived: {decrypted}")
            print("Message: ", end='', flush=True)
        except:
            break
    print("\nDisconnected from server")
    socket.close()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

client_key = RSA.generate(2048)
server_public_key = RSA.import_key(client.recv(2048))
client.send(client_key.publickey().export_key())

cipher_rsa = PKCS1_OAEP.new(client_key)
aes_key = cipher_rsa.decrypt(client.recv(2048))

receive_thread = threading.Thread(target=receive_messages, args=(client, aes_key))
receive_thread.daemon = True
receive_thread.start()

print("Connected! Start chatting...")
while True:
    try:
        message = input("Message: ")
        if message.lower() == 'exit':
            encrypted = encrypt_message(aes_key, message)
            client.send(encrypted)
            break
        encrypted = encrypt_message(aes_key, message)
        client.send(encrypted)
    except:
        break

client.close()