import pandas as pd
import os
from connection import connection,cursor


def set_categories():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    BASE_DIR = os.path.dirname(BASE_DIR)
    scraping_dir = os.path.join(BASE_DIR, "scraping")
    category_path = os.path.join(scraping_dir, "category.csv")
    subcategory_path = os.path.join(scraping_dir, "subcategory.csv")

    df_categories = pd.read_csv(category_path, header=None)
    df_subcategories = pd.read_csv(subcategory_path, header=None)
    for index, row in df_categories.iterrows():
        """
        For mssql:
        cursor.execute("INSERT INTO Categories (name) VALUES (?)", row[0])
        cursor.commit()
        """
        cursor.execute("INSERT INTO Categories (name) VALUES (?)", (row[0],))
        connection.commit()

    category_id = 1
    sub_id = 1
    for index,row in df_subcategories.iterrows():
        if row[1]==category_id:
            """
            For mssql:
            cursor.execute("INSERT INTO SubCategories (category_id,subcategory_id,name) VALUES (?,?,?)", row[1], sub_id, row[0])
            cursor.commit()
            """
            cursor.execute("INSERT INTO SubCategories (category_id,subcategory_id,name) VALUES (?,?,?)", (row[1], sub_id, row[0]))
            connection.commit()
            sub_id+=1
        else:
            category_id += 1
            sub_id = 1
            """
            For mssql:
            cursor.execute("INSERT INTO SubCategories (category_id,subcategory_id,name) VALUES (?,?,?)", row[1], sub_id, row[0])
            cursor.commit()
            """
            cursor.execute("INSERT INTO SubCategories (category_id,subcategory_id,name) VALUES (?,?,?)", (row[1], sub_id, row[0]))
            connection.commit()
            sub_id += 1

