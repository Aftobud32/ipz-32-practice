students_data = [
    {"name": "Іван", "grades": [4, 5, 3, 4, 5]},
    {"name": "Петро", "grades": [3, 3, 4, 3, 3]},
    {"name": "Ольга", "grades": [5, 5, 5, 5, 5]},
    {"name": "Назар", "grades": [4, 4, 5, 4, 5]}
]

student_averages = {}
all_grades_list = []

for student in students_data:
    name = student["name"]
    grades = student["grades"]
    
    avg = sum(grades) / len(grades)
    student_averages[name] = round(avg, 2)
    
    all_grades_list.extend(grades)

unique_grades = set(all_grades_list)

print("Середні бали студентів (Dict):", student_averages)
print("Унікальні оцінки (Set):", unique_grades)
print("Всі оцінки (List):", all_grades_list)