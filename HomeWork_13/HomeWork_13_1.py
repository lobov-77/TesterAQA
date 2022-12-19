class Person:

    def __init__(self):
        self.address = None
        self.phone = None
        self.age = None
        self.name = None
        self.surname = None

    def get_info(self, name: str, surname: str, age: int, phone_number: str, address: str):
        pass

    def get_info(self):
        pass

    def call(self, phone_number):
        pass


david = Person()
david.name = 'David'
david.surname = 'Backham'
david.age = 45
david.phone_number = '+44 2074012860'
david.address = 'London'

# tom = Person()
# tom.name = 'Tom'
# tom.surname = 'Cruise'
# tom.age = 60
# tom.phone_number = '+12 127363100'
# tom.address = 'New York'

# kylian = Person()
# kylian.name = 'Kylian'
# kylian.surname = 'Mbape'
# kylian.age = 23
# kylian.phone_number = '+33 140205050'
# kylian.address = 'Paris'


