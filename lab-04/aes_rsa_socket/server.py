from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

server_key = RSA.generate(2048)
clients = []

def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    cipher_text = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + cipher_text

def decrypt_message(key, encrypted_message):
    iv = encrypted_message[:AES.block_size]
    cipher_text = encrypted_message[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(cipher_text), AES.block_size)
    return decrypted_message

def broadcast(message, sender):
    for client in clients:
        if client[0] != sender:
            try:
                encrypted = encrypt_message(client[1], message.decode())
                client[0].send(encrypted)
            except:
                clients.remove(client)

def handle_client(client_socket, addr):
    print(f"New connection from {addr}")
    
    client_socket.send(server_key.publickey().export_key())
    client_public_key = RSA.import_key(client_socket.recv(2048))
    
    aes_key = get_random_bytes(16)
    cipher_rsa = PKCS1_OAEP.new(client_public_key)
    enc_aes_key = cipher_rsa.encrypt(aes_key)
    client_socket.send(enc_aes_key)
    
    clients.append((client_socket, aes_key))
    
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            
            decrypted = decrypt_message(aes_key, message)
            print(f"From {addr}: {decrypted.decode()}")
            
            if decrypted.decode() == "exit":
                break
                
            broadcast(decrypted, client_socket)
            
        except:
            break
            
    clients.remove((client_socket, aes_key))
    client_socket.close()
    print(f"Connection closed from {addr}")

print("Server is running...")
while True:
    client, addr = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(client, addr))
    thread.start()