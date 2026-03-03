class Car:
    def __init__(self, make, year, mileage):
        self.make = make
        self.year = year
        self._mileage = 0  # Initialize with 0 to use setter for validation
        self.mileage = mileage # Use setter for initialization

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, value):
        if value < 0:
            print(f"Помилка: Пробіг не може бути від'ємним ({value}). Залишено попереднє значення: {self._mileage}")
        elif value < self._mileage:
             print(f"Помилка: Пробіг не можна зменшити з {self._mileage} до {value}.")
        else:
            self._mileage = value

    def drive(self, km):
        if km > 0:
            self.mileage += km # Uses the setter
        else:
            print("Відстань має бути додатною")

    def __str__(self):
        return f"{self.make} ({self.year}) - {self.mileage} км"

print("--- Демонстрація властивостей Car ---")
c = Car("Toyota Camry", 2020, 50000)
print(c)

# Try setting negative mileage
print("\nСпроба встановити від'ємний пробіг:")
c.mileage = -100

# Try rolling back mileage
print("\nСпроба скрутити пробіг:")
c.mileage = 40000

# Valid update
print("\nКоректне оновлення:")
c.mileage = 50100
print(f"Оновлено: {c}")

print("\nПоїздка 200км:")
c.drive(200)
print(f"Після поїздки: {c}")