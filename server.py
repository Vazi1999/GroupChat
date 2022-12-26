from socket import AF_INET , socket , SOCK_STREAM
from threading import Thread
import time
from client import Person

# Sets the host and port to localhost.
HOST = 'localhost'
PORT = 5500
BUFSIZE = 512
ADDR = (HOST,PORT)
MAX_CONNECTIONS =5

persons = []
# Creates a socket and binds it to the server.
SERVER = socket(AF_INET,SOCK_STREAM)
SERVER.bind(ADDR)


# Broadcast a message to all persons.
def broadcast(msg , name):
    for person in persons:
        client = person.client
        client.send(bytes(name+ ":","utf8" )+msg)


# Receive a BUFSIZE message from the client.
def client_communication(person):
    
    client = person.client
    #get person name : 
    name = client.recv(BUFSIZE).decode('utf8')
    msg = f"{name} has been connected to the chat!"
    broadcast(msg)
    while True:
        try:
            msg = client.recv(BUFSIZE)
            print (f"{name}:",msg.decode('utf8'))
            if msg == bytes("{quit}","utf8"):
                broadcast(f"{name} has been disconnected",name)
                client.send(bytes("{quit}","utf8"))
                client.close()
                person.remove(person)
                break
            else:
                broadcast(msg,name)
        except Exception as e:
            print ("[FAILED] "+str(e))
            break




# Wait for a connection to be established.
def waiting_for_connection():
    run =True
    while run:
        try:
            client , clientAddress  = SERVER.accept()
            person = Person(clientAddress,client)
            persons.append(person)
            print(f"[CONNECTION] {ADDR} connected to the server at {time.time()}")
            Thread(target=client_communication , args=(person,)).start()
        except Exception as e:
            print ("[FAILED] Connection failes" , e)
            run = False
    print("SERVER CRASHED")



# Start the server and wait for it to finish.
if __name__ == '__main__':
    server.listen(MAX_CONNECTIONS)
    print("Waiting for server to start...")
    ACCEPT_THREAD = Thread(target=waiting_for_connection)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()

