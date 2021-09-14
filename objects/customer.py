class Customer:
    def __init__(self, id, first_name, last_name, phone, address):
        if id is None or id < 0:
            id = 0
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.address = address

    def display(self):
        print(f"\n\n\nID : {self.id}\nName : {self.first_name} {self.last_name}\nPhone : {self.phone}\n"
              f"Address : {self.address}\n\n")
