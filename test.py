class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


cars = [
    Car('Ford', 'Mustang', 2020),
    Car('Toyota', 'Camry', 2021),
    Car('Ford', 'F-150', 2022)
]

neighbors = [('Ford', 'Mustang')]


ford_cars = [index for index, car in enumerate(cars) if ((car.make, car.model) in neighbors) or (car.year == '2021')]
print(ford_cars)
