class Pet:
    def __init__(self, name, satiety=50, energy=50):
        self.name = name
        self.satiety = max(0, min(100, satiety))  
        self.energy = max(0, min(100, energy))   

    def sleep(self):
        self.energy = 100
        print(f"{self.name} спить. Енергія тепер {self.energy}.")

    def eat(self, food_amount):
        self.satiety = min(100, self.satiety + food_amount)  
        print(f"{self.name} їсть. Рівень ситості тепер {self.satiety}.")

    def play(self, activity_level):
        print(f"{self.name} грається, але метод play() не визначено для цього класу.")

    def make_sound(self):
        print(f"{self.name} видає звук, але метод make_sound() не визначено для цього класу.")

class Cat(Pet):
    def play(self, activity_level):
        if self.satiety > 60:
            self.energy = max(0, self.energy - 2 * activity_level)
            self.satiety = max(0, self.satiety - activity_level)
            print(f"{self.name} грається. Енергія: {self.energy}, ситість: {self.satiety}.")
        else:
            print(f"{self.name} занадто голодний, щоб гратися.")

    def make_sound(self):
        print("Мяу")

    def catch_mouse(self):
        if self.energy > 30:
            print(f"{self.name} ловить мишу.")
            if self.satiety > 40:
                self.play(10)  
            else:
                self.eat(20)  
        else:
            print(f"{self.name} занадто втомлений, щоб ловити мишу.")

class Dog(Pet):
    def play(self, activity_level):
        if self.satiety > 15:
            self.energy = max(0, self.energy - activity_level // 2)
            self.satiety = max(0, self.satiety - activity_level // 2)
            print(f"{self.name} грається. Енергія: {self.energy}, ситість: {self.satiety}.")
        else:
            print(f"{self.name} занадто голодний, щоб гратися.")

    def make_sound(self):
        print("Гав")

    def fetch_ball(self):
        if self.satiety > 10:
            self.energy = max(0, self.energy - 5)
            print(f"{self.name} ловить м'яч. Енергія тепер {self.energy}.")
        else:
            print(f"{self.name} занадто голодний, щоб ловити м'яч.")

my_cat = Cat(name="Барсик")
my_dog = Dog(name="Шарик")

my_cat.make_sound()  
my_cat.play(15)  
my_cat.catch_mouse()  

my_dog.make_sound()  
my_dog.play(20)  
my_dog.fetch_ball()  
