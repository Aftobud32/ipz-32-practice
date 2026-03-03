from library_item import LibraryItem

class Book(LibraryItem):
    def __init__(self, title, item_id, author, pages):
        super().__init__(title, item_id)
        self.author = author
        self.pages = pages

    def get_details(self):
        return f"Книга: {self.title}, Автор: {self.author}, {self.pages} сторінок"