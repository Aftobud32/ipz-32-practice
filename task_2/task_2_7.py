class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Гав")

class Cat(Animal):
    def sound(self):
        print("Мяу")

class Cow(Animal):
    def sound(self):
        print("Му")

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()

print("\nПояснення:")
print("Python використовує пізнє зв'язування (динамічну диспетчеризацію). Конкретна реалізація методу")
print("визначається під час виконання на основі фактичного типу об'єкта, а не типу змінної.")