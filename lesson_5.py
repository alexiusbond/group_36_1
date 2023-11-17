from random import randint as generate_number, choice
import calculator
from person import Person
from termcolor import cprint
import emoji
from decouple import config

print(generate_number(2, 10))
print(calculator.multiplication(9, 2))

friend = Person('Jim', 33)
print(friend)
cprint("Hello, World!", "green", "on_red")
print(emoji.emojize('Python is :thumbs_up:'))

print(config('DATABASE_URL'))

commented = config('COMMENTED', default=0, cast=int)
print(commented)
print(commented * 2)
# The end
