# class

class Car:
    #constructor
    def __init__(self, _colour, _make):
        self._colour = _colour
        self._make = _make

        print("Hello")

    def get_colour(self):
        return self._colour
    
    def set_colour(self, _colour):
        self._colour = _colour
    
    def run(self):
        print(f"{self._make} is running!!")

#object
my_car = Car("White", "Honda")

print(my_car)
print(my_car._colour)
print(my_car._make)

print(my_car.get_colour())

my_car.run()

your_car = Car("Black", "Holden")
your_car.run()

my_car.set_colour("Blue")
print(my_car.get_colour())


class PetrolCar(Car):
    def __init__(self, _colour, _make, _capacity_of_tank):
        super().__init__(_colour, _make)
        self._capacity_of_tank = _capacity_of_tank

    def get_capacity(self):
        return self._capacity_of_tank
        
petrol_car = PetrolCar("Green", "BMW", "35L")
petrol_car.run()

print(petrol_car.get_capacity())

class ElectricCar(Car):
    # pass

    def run(self):
        print("RUNNNNNN")

electric = ElectricCar("gegee", "fdssd")

electric.run()
print(electric.get_colour())