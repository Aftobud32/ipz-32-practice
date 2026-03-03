from library_item import LibraryItem

class DVD(LibraryItem):
    def __init__(self, title, item_id, director, duration):
        super().__init__(title, item_id)
        self.director = director
        self.duration = duration

    def get_details(self):
        return f"DVD: {self.title}, Режисер: {self.director}, {self.duration} хв"