class Contact:
    def __init__(self, city, street, number):
        self.__city = city
        self.__street = street
        self.__number = number

    @property
    def city(self):
        return self.__city

    @property
    def street(self):
        return self.__street

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value


class Animal:
    def __init__(self, name, age, contact):
        self.__name = name
        if type(age) == int and age > 0:
            self.__age = age
        else:
            raise ValueError('Wrong value for attribute age. It must be positive number!')
        if type(contact) == Contact:
            self.__contact = contact
        else:
            raise ValueError('Wrong value for attribute contact. It must be of data type Contact!')
        self.__was_born()

    def __was_born(self):
        print(f'Animal {self.__name} was born!!!')

    def set_age(self, new_age):
        if type(new_age) == int and new_age > 0:
            self.__age = new_age
        else:
            raise ValueError('Wrong value for attribute age. It must be positive number!')

    def set_name(self, new_name):
        self.__name = new_name

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def info(self):
        return (f'NAME: {self.__name} AGE: {self.__age} '
                f'BIRTH YEAR: {2023 - self.__age}\n'
                f'CONTACT INFO: {self.__contact.city} '
                f'{self.__contact.street}, {self.__contact.number}')

    def make_voice(self):
        raise NotImplementedError('Method make_voice must be implemented')


class Dog(Animal):
    def __init__(self, name, age, commands, contact):
        super(Dog, self).__init__(name, age, contact)
        self.__commands = commands

    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, value):
        self.__commands = value

    def info(self):
        return super().info() + f'\nCOMMANDS: {self.__commands}'

    def make_voice(self):
        print('Gav')


class FightingDog(Dog):
    def __init__(self, name, age, commands, wins, contact):
        super(FightingDog, self).__init__(name, age, commands, contact)
        self.__wins = wins

    @property
    def wins(self):
        return self.__wins

    @wins.setter
    def wins(self, value):
        self.__wins = value

    def info(self):
        return super().info() + f'\nWINS: {self.__wins}'

    def make_voice(self):
        print('Rrrrr gav')


class Cat(Animal):
    def __init__(self, name, age, contact):
        super(Cat, self).__init__(name, age, contact)

    def make_voice(self):
        print('Myau')

class Fish(Animal):
    def __init__(self, name, age, contact):
        super(Fish, self).__init__(name, age, contact)

    def make_voice(self):
        pass

# some_animal = Animal('Anim', 2, contact_1)
# print(some_animal.info())
# # some_animal.__age = -4
# some_animal.set_age(4)
# print(some_animal.info())
# print(some_animal.get_name())

contact_1 = Contact('Bishkek', 'Isanova', 9)
#       a = b

bobik_dog = Dog('Bobik', 10, 'Sit', contact_1)
print(bobik_dog.commands)
bobik_dog.commands = 'Sit, run'

tom_cat = Cat('Tom', 3,
              Contact('Osh', 'Lenina', 1))

reks_f_dog = FightingDog('Reks', 1,
                         'Fight', 15, contact_1)

nemo_fish = Fish('Nemo', 4, contact_1)

animals_list = [bobik_dog, tom_cat, nemo_fish, reks_f_dog]
for animal in animals_list:
    print(animal.info())
    animal.make_voice()
