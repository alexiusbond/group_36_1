from enum import Enum


class Color(Enum):
    RED = '\33[31m'
    BLUE = '\33[34m'
    YELLOW = '\33[33m'
    GREEN = '\33[32m'


class MusicPlayable:

    @staticmethod
    def play_music(song):
        print(f'Now is playing {song}')

    @staticmethod
    def stop_music():
        print('Music stopped')


class Drawable:
    @staticmethod
    def draw(emoji):
        print(emoji)


class SmartPhone(MusicPlayable, Drawable):
    # def __init__(self):
    #     pass
    pass


class Car(MusicPlayable, Drawable):
    def __init__(self, model, year, color):
        self.__model = model
        self.__year = year
        if type(color) == Color:
            self.__color = color

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    def drive(self):
        print(f'Car {self.__model} is driving')

    def __str__(self):
        return (f'MODEL: {self.__model} YEAR: {self.__year} '
                f'COLOR: {self.__color.value}{self.__color.name}'
                + '\33[0m')

    def __gt__(self, other):
        return self.__year > other.__year

    def __lt__(self, other):
        return self.__year < other.__year

    def __ge__(self, other):
        return self.__year >= other.__year

    def __le__(self, other):
        return self.__year <= other.__year

    def __eq__(self, other):
        return self.__year == other.__year

    def __ne__(self, other):
        return self.__year != other.__year


class FuelCar(Car):
    __total_fuel_amount = 1000

    @staticmethod
    def get_fuel_type():
        return 'AI 95'

    @classmethod
    def get_total_fuel_amount(cls):
        return cls.__total_fuel_amount

    @classmethod
    def fill_total_fuel_amount(cls, amount):
        cls.__total_fuel_amount += amount

    def __init__(self, model, year, color, fuel_bank):
        Car.__init__(self, model, year, color)
        self.__fuel_bank = fuel_bank
        FuelCar.__total_fuel_amount -= fuel_bank

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    def drive(self):
        print(f'Car {self.model} is driving by using fuel')

    def __str__(self):
        return super().__str__() + f' FUEL BANK: {self.__fuel_bank} lt.'

    def __add__(self, other):
        return self.__fuel_bank + other.__fuel_bank


class ElectricCar(Car):
    def __init__(self, model, year, color, battery):
        Car.__init__(self, model, year, color)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    def drive(self):
        print(f'Car {self.model} is driving by using electricity')

    def __str__(self):
        return super().__str__() + f' BATTERY: {self.__battery}'


class HybridCar(FuelCar, ElectricCar):
    def __init__(self, model, year, color, fuel_bank, battery):
        FuelCar.__init__(self, model, year, color, fuel_bank)
        ElectricCar.__init__(self, model, year, color, battery)


print(f'We have {FuelCar.get_total_fuel_amount()} lt. '
      f'({FuelCar.get_fuel_type()}) on FUEL CARS FABRIC')

bmw_car = Car('BMW X6', 2020, Color.RED)
print(bmw_car)

nissan_car = FuelCar('Nissan Patrol', 2009,
                     Color.YELLOW, 85)
print(nissan_car)

tesla_car = ElectricCar('Tesla Model X', 2023,
                        Color.GREEN, 25000)
print(tesla_car)

toyota_car = HybridCar('Toyota Prius', 2009,
                       Color.BLUE, 65, 15000)
print(toyota_car)
toyota_car.drive()
print(HybridCar.mro())

number_1 = 7
number_2 = 3
print(f'Number one is bigger than number two? --> {number_1 > number_2}')
print(f'Number two is bigger than number one? --> {number_2 > number_1}')

print(f'Nissan car is better than Tesla car? --> {nissan_car > tesla_car}')
print(f'Nissan car is the same with Toyota car? --> {nissan_car == toyota_car}')

print(f'Sum of numbers: {number_1 + number_2}')
print(f'Total fuel banks amount: {nissan_car + toyota_car} lt.')

# FuelCar.total_fuel_amount -= 100
FuelCar.fill_total_fuel_amount(500)
print(f'We have {FuelCar.get_total_fuel_amount()} lt. '
      f'({FuelCar.get_fuel_type()}) on FUEL CARS FABRIC')

tesla_car.play_music('Song 1')
tesla_car.stop_music()

samsung = SmartPhone()
samsung.play_music('Best Song')

toyota_car.draw('🚗')
samsung.draw('📱')

if tesla_car.model == 'Tesla Model X':
    print('This car is cool!')


if tesla_car.color == Color.GREEN:
    print('This car is beautiful!')
