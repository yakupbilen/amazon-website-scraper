import selenium.common.exceptions
from selenium import webdriver
import time
from scraping.get_product_from_amazon_page import getProducts
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def openMenu(browser, category, subCategory):
    try:
        time.sleep(0.75)
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='nav-hamburger-menu']"))).click()
        categoryText = ""
        if category > 10:
            time.sleep(0.75)
            seeAll = browser.find_element_by_css_selector("#hmenu-content > ul.hmenu-visible > li:nth-child(12) > a")
            try:
                seeAll.click()
            except selenium.common.exceptions.ElementNotInteractableException:
                pass
            time.sleep(0.75)
            categorySelector = "div#hmenu-content > ul.hmenu-visible > ul > li:nth-child({}) > a".format(category - 9)
            categorySelection = browser.find_element_by_css_selector(categorySelector)
            categoryText = categorySelection.text
            categorySelection.click()

        else:
            time.sleep(0.75)
            categorySelector = "div#hmenu-content > ul.hmenu-visible > li:nth-child({}) > a".format(category)
            categorySelection = browser.find_element_by_css_selector(categorySelector)
            categoryText=categorySelection.text
            WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, categorySelector))).click()

        time.sleep(1)
        subCategorySelector = "div#hmenu-content > ul.hmenu-visible > li:nth-child({}) > a".format(subCategory)
        subCategorySelection = browser.find_element_by_css_selector(subCategorySelector)
        subText=subCategorySelection.text
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, subCategorySelector))).click()

        if subCategory == 3:
            dictCat = {"Category":categoryText}
            list = []
            list.append(dictCat)
            df = pd.DataFrame(list)
            df.to_csv("category.csv",index=False,header=False,mode="a")
        list =[]
        dictSub = {"SubCategory": subText, "CategoryId": category - 6}
        list.append(dictSub)
        df2=pd.DataFrame(list)
        df2.to_csv("subcategory.csv",index=False,header=False,mode="a")

        productList = getProducts(browser, category-6, subCategory-2)
        productDictList = []
        for product in productList:
            productDictList.append({"Name":product.name,"Price":product.price,"Stock":product.stock,"Category":product.category,"SubCategory":product.subcategory,"ImagePath":product.image})
        df = pd.DataFrame(productDictList)
        df.to_csv("product.csv",index=False,header=False,mode="a")
    except selenium.common.exceptions.NoSuchElementException:
        try:
            WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#hmenu-canvas-background > div"))).click()
        except selenium.common.exceptions.TimeoutException:
            pass
        return False


browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.amazon.com")
time.sleep(1)

for i in range(7,29):
    j=3
    while True:
        if openMenu(browser,i,j)==False:
            break
        j+=1

