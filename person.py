# Returns a human - readable description of the Person.

class Person:
    def __init__(self,address,client):
        self.address = address
        self.client = client
        self.name = None

    def set_name(self,name):
        self.name = name

    def __repr__(self):
        return (f"Person({self.address},{self.name})")
        



