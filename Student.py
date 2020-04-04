class Student:

    def __init__(self, name, identity):
        self.identity = identity
        self.name = name

    def __str__(self):
        return 'Name: '+self.name+', Identity number: '+str(self.identity)

    def getname(self):
        return self.name

    def getidentity(self):
        return self.identity
