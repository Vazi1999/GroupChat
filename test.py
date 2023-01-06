from client import Client
import time
from threading import Thread

c1 = Client("Ofek")
c2 = Client("Shaked")



# Updates the list of messages and prints them.
def update_messages():
    msgs = []
    run = True
    while run:
        time.sleep(0.1)
        new_messages = c1.get_messages()
        msgs.extend(new_messages)
        for msg in new_messages:
            print(msg)
            if msg=="{quit}":
                run=False
                break

Thread(target=update_messages).start()



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