from client import Client
import time
from threading import Thread

c1 = Client("Ofek")
c2 = Client("Shaked")

c1.send_messages("hello")
time.sleep(1)
c2.send_messages("hello to you to")
time.sleep(1)
c1.send_messages("whats up")
time.sleep(1)
c2.send_messages("nothing much")
time.sleep(5)

c1.disconnect()
time.sleep(2)
c2.disconnect()

def update_messages():
    pass
