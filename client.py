import socket

class Person:
    def __init__(self,address,client):
        self.address = address
        self.client = client
        self.name = None

    def set_name(self,name):
        self.name = name



    def __repr__(self):
        return (f"Person({self.address},{self.name})")
        


HOST = 'localhost'
PORT = 8000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    data = client.recv(1024)
    if not data:
        break
    print(data.decode())
    message = input('> ')
    client.send(message.encode())

client.close()
