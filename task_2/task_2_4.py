class Car:
    def __init__(self, make, year, mileage):
        self.make = make
        self.year = year
        self.mileage = mileage

    def drive(self, km):
        if km > 0:
            self.mileage += km

    def info(self):
        print(f"Авто: {self.make}, Рік: {self.year}, Пробіг: {self.mileage} км")

    def __str__(self):
        return f"{self.make} ({self.year}) - {self.mileage} км"

c = Car("Toyota Camry", 2020, 50000)
c.info()
print(f"Рядкове представлення: {c}")

c.drive(150)
print(f"Після поїздки 150км: {c}")