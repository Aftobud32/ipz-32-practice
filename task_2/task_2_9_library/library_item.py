from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.is_checked_out = False

    @abstractmethod
    def get_details(self):
        pass

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False

    def return_item(self):
        self.is_checked_out = False