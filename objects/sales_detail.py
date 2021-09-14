class SalesDetail:
    def __init__(self,id,sales_id,product_id,amount,price):
        if id is None:
            id = 0
        self.id = id
        self.sales_id = sales_id
        self.product_id = product_id
        self.amount = amount
        self.price = price

    def display(self):
        print(f"Id : {self.id}\nFiche Id : {self.sales_id}\nProduct Id : {self.product_id}\nAmount : {self.amount}\nPrice : {self.price}")