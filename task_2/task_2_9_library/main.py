from book import Book
from dvd import DVD
from patron import Patron

book1 = Book("Великий Гетсбі", "B001", "Ф. Скотт Фіцджеральд", 180)
dvd1 = DVD("Початок", "D001", "Крістофер Нолан", 148)

patron1 = Patron("Аліса", "P001")
patron2 = Patron("Боб", "P002")

print(book1.get_details())
print(dvd1.get_details())

patron1.borrow_item(book1)
patron2.borrow_item(book1)

patron1.return_item(book1)
patron2.borrow_item(book1)