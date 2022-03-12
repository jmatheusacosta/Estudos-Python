class Animal:
    paws_number = 4

    def __init__(self, name, size, type, habitat):
        self.name = name
        self.size = size
        self.type = type
        self.habitat = habitat

    def breathe(self):
        print("Esse "+ self.name+ " está respirando")