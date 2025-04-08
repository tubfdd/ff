from re import search

from bintrees import AVLTree

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


class CarPark:
    def __init__(self):
        self.cars = AVLTree()

    def __len__(self):
        return len(self.cars)

    def add(self, car):
        self.cars.insert(key=car.model,value=car)

    def search(self, model):
        if model in self.cars:
            return self.cars[model]
        else:
            return None

    def remove(self, model):
        if self.search(model) != None:
            self.cars.remove(model)
        else:
            print(f'Автомобіля моделі {model} немає в гаражі, тому видалити його неможливо.')


    def sell_car(self, client, model):
        car_for_sell = self.search(model)
        if car_for_sell != None:
            self.remove(model)
            print(f"Клієнту {client} продано автомобіль {car_for_sell.brand}, {car_for_sell.model}, {car_for_sell.year}.")
        else:
            print(f'Автомобіля моделі {model} немає в гаражі, тому його продати неможливо.')


car1 = Car('Mercedes','dqwd',2011)
car2 = Car('BMW','scc',2023)
car3 = Car('Renault','gergfer',2022)
car4 = Car('Toyota','mdkw',2012)
car5 = Car('Skoda','kxmw',2019)

car_garage = CarPark()

car_garage.add(car1)
car_garage.add(car2)
car_garage.add(car3)
car_garage.add(car4)
car_garage.add(car5)
print(f"Авто в гаражі: {len(car_garage)}")

car_garage.remove('mdkw')
print(f"Авто в гаражі: {len(car_garage)}")
car_garage.sell_car("Ivan",'mdkw')
print(f"Авто в гаражі: {len(car_garage)}")
