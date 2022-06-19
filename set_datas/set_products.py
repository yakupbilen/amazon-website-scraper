from connection import cursor,connection
import pandas as pd
import sql_queries
import os


def read_image(file):
    with open(file, 'rb') as file:
        image = file.read()
    return image


def set_products():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    BASE_DIR = os.path.dirname(BASE_DIR)
    scraping_dir = os.path.join(BASE_DIR, "scraping")
    product_path = os.path.join(scraping_dir, "product.csv")

    df_products = pd.read_csv(product_path, header=None)
    df_products.dropna(inplace=True)

    image_paths = df_products[5]

    del df_products[5]

    image_paths = image_paths.apply(read_image)

    df = pd.concat([df_products,image_paths],axis=1)
    list_products = df.values.tolist()

    cursor.executemany(sql_queries.insert_product,list_products)
    """
    cursor.commit()
    """

    connection.commit()