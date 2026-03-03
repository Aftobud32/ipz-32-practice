class Animal:
    def sound(self):
        print("Якийсь звук тварини")

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