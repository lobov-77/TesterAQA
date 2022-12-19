class Human:
    def __init__(self, name, surname, age, phone, address):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.address = address

    def get_info(self):
        return {
            'name': self.name,
            'surname': self.surname,
            'age': self.age,
            'phone': self.phone,
            'address': self.address
        }

    def call(self, phone_number):
        print(f"{self.phone} вызывает абонента {phone_number}")


david = Human(
    name='David',
    surname='Backham',
    age=45,
    phone='+44 2074012860',
    address='London')

tom = Human(
    name='Tom',
    surname='Cruise',
    age=60,
    phone='+12 127363100',
    address='New York')

kylian = Human(
    name='Kylian',
    surname='Mbape',
    age=23,
    phone='+33 140205050',
    address='Paris')

print(david.get_info())
print(tom.get_info())
print(kylian.get_info())

print((david.call('875897587')))
