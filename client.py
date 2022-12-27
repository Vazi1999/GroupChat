from socket import AF_INET , socket , SOCK_STREAM
from threading import Thread,Lock



class Client:

    HOST = 'localhost'
    PORT = 5500
    ADDRESS = (HOST, PORT)
    BUFSIZE = 512

    def __init__(self,name):
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(self.ADDRESS)
        self.messages = []      
        recieve_thread = Thread(target=self.recieve_messages)
        recieve_thread.start()
        self.send_messages(name)
        self.lock=Lock()


    # Receive messages from the server.
    def recieve_messages(self):
        while True:
            try:
                msg = self.client_socket.recv(self.BUFSIZE).decode('utf-8')
                self.lock.acquire()
                self.messages.append(msg)
                self.lock.release()
            except Exception as e:
                print("[FAILED]",e)
                break


    # Sends a message to the server.
    def send_messages(self,msg):
        self.client_socket.send(bytes(msg,"utf-8"))
        if msg == "{quit}":
            self.client.close()

    # Returns a list of messages.
    def get_messages(self):
        self.lock.acquire()
        self.lock.release()
        return self.messages

    def disconnect(self):
        self.send_messages(bytes("{quit}"),"utf-8")