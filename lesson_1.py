class Transport:
    def __init__(self, theYear, theModel, theColor):
        self.year = theYear
        self.model = theModel
        self.color = theColor

    def change_color(self, new_color):
        self.color = new_color


class Plane(Transport):
    def __init__(self, theYear, theModel, theColor):
        super().__init__(theYear, theModel, theColor)


class Car(Transport):
    # class attribute
    counter = 0
    wheels_num_by_standart = 5

    # contructor
    def __init__(self, theYear, theModel, theColor, penalties=0):
        # fields/attributes
        super().__init__(theYear, theModel, theColor)
        self.penalties = penalties
        Car.counter += 1

    # method
    def drive(self, city):
        print(f'Car {self.model} is driving to {city}')


class Truck(Car):
    wheels_num_by_standart = 10
    def __init__(self, theYear, theModel, theColor, penalties=0, load_capacity=0):
        super().__init__(theYear, theModel, theColor, penalties)
        self.load_capacity = load_capacity

    def load_cargo(self, weight, type):
        if weight > self.load_capacity:
            print(f'You can not load more than {self.load_capacity} kg')
        else:
            print(f'Cargo of {type} ({weight} kg) was successfuly '
                  f'loaded on {self.model}')


price_of_lastic = 5000
print(f'We produced {Car.counter} cars on CAR factory.')
print(f'We need {price_of_lastic * Car.wheels_num_by_standart * Car.counter} '
      f'soms to buy winter lastics.')

bmw_car = Car(2020, 'BMW X6', 'Red')
print(bmw_car)
print(f'MODEL: {bmw_car.model} YEAR: {bmw_car.year} COLOR: {bmw_car.color} '
      f'PENALTIES: {bmw_car.penalties}')
# bmw_car.color = 'Black'
bmw_car.change_color('Black')
print(f'MODEL: {bmw_car.model} YEAR: {bmw_car.year} '
      f'NEW COLOR: {bmw_car.color} PENALTIES: {bmw_car.penalties}')

honda_car = Car(theModel='Honda CR-V',
                theColor='White', penalties=1000, theYear=2009)
print(f'MODEL: {honda_car.model} YEAR: {honda_car.year} '
      f'COLOR: {honda_car.color} PENALTIES: {honda_car.penalties}')
honda_car.drive('Osh')
bmw_car.drive('Kant')
bmw_car.drive('Tokmok')

print(f'We produced {Car.counter} cars on CAR factory.')
print(f'We need {price_of_lastic * Car.wheels_num_by_standart * Car.counter} '
      f'soms to buy winter lastics.')

boeing_plane = Plane(2022, 'Boeing 747', 'Blue')
print(f'MODEL: {boeing_plane.model} YEAR: {boeing_plane.year} '
      f'COLOR: {boeing_plane.color}')

daf_truck = Truck(2019, 'DAF 33', 'Green',
                  500, 35000)
print(f'MODEL: {daf_truck.model} YEAR: {daf_truck.year} '
      f'COLOR: {daf_truck.color} PENALTIES: {daf_truck.penalties} '
      f'LOAD CAPACITY: {daf_truck.load_capacity} kg')
daf_truck.load_cargo(40000, 'tomatoes')
daf_truck.load_cargo(20000, 'apples')
daf_truck.drive('Batken')

print(f'Truck has {Truck.wheels_num_by_standart} wheels.')