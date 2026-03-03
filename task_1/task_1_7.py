class Student:
    def __init__(self, first_name, last_name, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades

students = [
    Student("Іван", "Іванов", [4, 5, 3, 4, 5]),
    Student("Петро", "Петров", [3, 3, 4, 3, 3]),
    Student("Ольга", "Сидорова", [5, 5, 5, 5, 5]),
    Student("Назар", "Клокун", [4, 4, 5, 4, 5])
]

print(f"{'Ім\'я':<20} {'Оцінки':<15} {'Сер.':<5}")
print("-" * 45)

for s in students:
    avg = sum(s.grades) / len(s.grades)
    grades_str = " ".join(map(str, s.grades))
    full_name = f"{s.first_name} {s.last_name}"
    print(f"{full_name:<20} {grades_str:<15} {avg:.2f}")

print("-" * 45)

num_subjects = 5
subject_avgs = []
for i in range(num_subjects):
    col_sum = sum(s.grades[i] for s in students)
    subject_avgs.append(col_sum / len(students))

print("Середній бал групи з предметів:", end=" ")
for avg in subject_avgs:
    print(f"{avg:.2f}", end=" ")
print()