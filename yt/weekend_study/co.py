class Person :
    def __init__(self,name):#constructor
        self.name=name
    def talk(self):
        print(f"hi, I am  {self.name} ")

ropy = Person("ropy kevin")
ropy.talk()
bob =Person("Bob smith")
bob.talk()