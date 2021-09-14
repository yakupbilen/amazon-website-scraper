import sql_queries
from connection import cursor

class Product:
    def __init__(self, id, name, price, stock, category, subcategory, image):
        if id is None or id < 0:
            id = 0
        if price < 0:
            price = 0.99
        if stock < 0:
            stock = 0
        self.image = image
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category
        self.subcategory = subcategory

    def display(self):
        """
        cursor.execute(sql_queries.select_categories_id,self.category)
        category_name = cursor.fetchone()
        cursor.execute(sql_queries.select_sub_categories,self.category,self.subcategory)
        subcategory_name = cursor.fetchone()
        """
        cursor.execute(sql_queries.select_categories_id,(self.category,))
        category_name = cursor.fetchone()
        cursor.execute(sql_queries.select_sub_categories,(self.category,self.subcategory))
        subcategory_name = cursor.fetchone()
        print(f"\n\nID : {self.id}\nName : {self.name}\nPrice : {self.price}\nStock : {self.stock}\n"
              f"Category : {category_name[0]}\nSubcategory : {subcategory_name[0]}\n\n")
