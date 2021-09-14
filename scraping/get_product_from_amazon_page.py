from objects.product import Product
from random import randint,random
import urllib.request
import selenium.common.exceptions
import os
import socket

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")

def randomPrice():
    return round(random()*500,2)

def randomStock():
    return randint(20,200)

def getProducts(browser, category, subcategory):
    stopwords = []
    deletewords=[]
    with open("stopwordsamazon.txt", "r", encoding="utf-8") as file:
        stopwords=file.readlines()
    with open("deletewords.txt", "r", encoding="utf-8") as file:
        deletewords = file.readlines()

    product = browser.find_elements_by_xpath("//div[@id='search']/div[1]/div[1]/div[1]/span[3]/div[2]/div")
    if len(product) == 0:
        product = browser.find_elements_by_xpath("//div[@id='search']/div[1]/div[1]/div/span[3]/div[2]/div")
    if len(product) == 0:
        product = browser.find_elements_by_xpath("//*[@id='search']/div[1]/div/div[1]/div/span[3]/div[2]/div")


    list = []
    for i in product:
        try:
            image = i.find_element_by_class_name("s-image")
            imageUrl = image.get_attribute("src")
            imagePath = (image.get_attribute("src")).split("/")[-1]
            list.append([i.text,imageUrl,os.path.join(image_dir, imagePath)])
        except selenium.common.exceptions.NoSuchElementException:
            pass

    clean_list=[]
    index = 0
    for item in list:
        tempText = item[0]
        inDelete = False
        for delete in deletewords:
            if item[0].__contains__(delete.strip()):
                inDelete=True
                continue
        for stop in stopwords:
            tempText=tempText.replace(stop,"")
        if not inDelete:
            clean_list.append([tempText,item[1],item[2]])
        index+=1
    productList=[]
    index = 0
    for i in clean_list:
        productAttributes = i[0].splitlines()
        if len(productAttributes) > 0:
            name = productAttributes[0]
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
                if (len(productAttributes) > 3) & image_down:
                    try:
                        price = productAttributes[2].strip()
                        comma = productAttributes[3].strip()
                        price = float(price[1:]) + float(float(comma[0:2]) / 100)
                        price = round(price, 2)
                        productList.append(Product(None, name, price, randomStock(), category, subcategory, image=i[2]))
                    except ValueError:
                        productList.append(Product(None, name, randomPrice(), randomStock(), category, subcategory, image=i[2]))
                else:
                    productList.append(
                        Product(None, productAttributes[0], randomPrice(), randomStock(), category, subcategory, image=i[2]))

        index += 1
    return productList
    """for p in productList:
        print(f'Name : {p.name}\nPrice : {p.price}\nStock : {p.stock}\nCategory : {p.category}\nSubCategory : {p.subcategory}\n')
"""
