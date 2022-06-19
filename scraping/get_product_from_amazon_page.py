from objects.product import Product
from random import randint
import urllib.request
import selenium.common.exceptions
import os
import socket

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")


def get_products(browser, category, subcategory):
    with open("scraping/stopwordsamazon.txt", "r", encoding="utf-8") as file:
        stop_words = file.readlines()
    with open("scraping/deletewords.txt", "r", encoding="utf-8") as file:
        delete_words = file.readlines()

    product = browser.find_elements_by_xpath("//div[@id='search']/div[1]/div[1]/div[1]/span[3]/div[2]/div")
    if len(product) == 0:
        product = browser.find_elements_by_xpath("//div[@id='search']/div[1]/div[1]/div/span[3]/div[2]/div")
    if len(product) == 0:
        product = browser.find_elements_by_xpath("//*[@id='search']/div[1]/div/div[1]/div/span[3]/div[2]/div")

    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
    product_list = []
    for i in product:
        try:
            image = i.find_element_by_class_name("s-image")
            image_url = image.get_attribute("src")
            image_path = (image.get_attribute("src")).split("/")[-1]
            product_list.append([i.text,image_url,os.path.join(image_dir, image_path)])
        except selenium.common.exceptions.NoSuchElementException:
            pass

    clean_list = []
    index = 0
    for item in product_list:
        temp_text = item[0]
        in_delete = False
        for delete in delete_words:
            if item[0].__contains__(delete.strip()):
                in_delete=True
                continue
        for stop in stop_words:
            temp_text=temp_text.replace(stop,"")
        if not in_delete:
            clean_list.append([temp_text,item[1],item[2]])
        index+=1
    product_list=[]
    index = 0
    for i in clean_list:
        product_attributes = i[0].splitlines()
        if len(product_attributes) > 0:
            name = product_attributes[0]
            if not name.__contains__("Sponsored"):
                image_down = False
                try:
                    urllib.request.urlretrieve(i[1], i[2])
                    image_down = True
                except urllib.error.ContentTooShortError as shortError:
                    print("content too short error")
                except urllib.error.HTTPError as ex:
                    print(ex)
                except urllib.error.URLError:
                    print("fail to download!")
                except socket.timeout:
                    pass
                if (len(product_attributes) > 3) & image_down:
                    try:
                        price = product_attributes[2].strip()
                        comma = product_attributes[3].strip()
                        price = float(price[1:]) + float(float(comma[0:2]) / 100)
                        price = round(price, 2)
                        product_list.append(Product(None, name, price, random_stock(), category, subcategory, image=i[2]))
                    except ValueError:
                        pass
        index += 1
    """
        for p in productList:
            print(f'Name : {p.name}\nPrice : {p.price}\nStock : {p.stock}\nCategory : {p.category}\nSubCategory : {p.subcategory}\n')
        """

    return product_list


def random_stock():
    return randint(20,200)
