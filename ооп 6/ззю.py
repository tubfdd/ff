class Passenger:
    def __init__(self, name, destination):
        self.name = name
        self.destination = destination

class Transport:
    def __init__(self, speed):
        self.speed = speed

    def move(self, destination, distance):
        travel_time = distance / self.speed
        print(f"Рухаємося до {destination}. Це займе {travel_time:.2f} годин.")

class Bus(Transport):
    def __init__(self, speed, capacity):
        super().__init__(speed)
        self.passengers = []
        self.capacity = capacity

    def board_passenger(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            print(f"Пасажир {passenger.name} доданий до автобуса.")
        else:
            print("Немає місця для пасажира.")

    def move(self, destination, distance):
        disembarking_passengers = [p for p in self.passengers if p.destination == destination]
        self.passengers = [p for p in self.passengers if p.destination != destination]

        print(f"Висаджуємо {len(disembarking_passengers)} пасажирів у {destination}.")
        for passenger in disembarking_passengers:
            print(f"Пасажир {passenger.name} висаджений.")

        super().move(destination, distance)


passenger1 = Passenger("Олександр", "Київ")
passenger2 = Passenger("Ірина", "Львів")
passenger3 = Passenger("Михайло", "Київ")

bus = Bus(speed=60, capacity=2)

bus.board_passenger(passenger1)
bus.board_passenger(passenger2)
bus.board_passenger(passenger3) 

bus.move("Київ", 300)

bus.move("Львів", 600)