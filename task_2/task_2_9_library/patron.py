class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.checked_out_items = []

    def borrow_item(self, item):
        if item.check_out():
            self.checked_out_items.append(item)
            print(f"{self.name} позичив {item.title}")
        else:
            print(f"{item.title} вже видано")

    def return_item(self, item):
        if item in self.checked_out_items:
            item.return_item()
            self.checked_out_items.remove(item)
            print(f"{self.name} повернув {item.title}")
        else:
            print(f"{self.name} не має {item.title}")