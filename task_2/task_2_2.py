class Student:
    def __init__(self, name, group, avg_grade):
        self.name = name
        self.group = group
        self.avg_grade = avg_grade

    def show_info(self):
        print(f"Ім'я: {self.name}, Група: {self.group}, Середній бал: {self.avg_grade}")

s1 = Student("Іван Іванов", "ІПЗ-32", 4.5)
s2 = Student("Петро Петров", "ІПЗ-31", 3.8)
s3 = Student("Ольга Сидорова", "ІПЗ-32", 5.0)

s1.show_info()
s2.show_info()
s3.show_info()