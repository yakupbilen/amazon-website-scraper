import selenium.common.exceptions
import time
from scraping.get_product_from_amazon_page import get_products
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def open_menu(browser, category, sub_category):
    try:
        time.sleep(0.75)
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='nav-hamburger-menu']"))).click()
        category_text = ""
        if category > 10:
            time.sleep(0.75)
            see_all = browser.find_element_by_css_selector("#hmenu-content > ul.hmenu-visible > li:nth-child(12) > a")
            try:
                see_all.click()
            except selenium.common.exceptions.ElementNotInteractableException:
                pass
            time.sleep(0.75)
            category_selector = "div#hmenu-content > ul.hmenu-visible > ul > li:nth-child({}) > a".format(category - 9)
            category_selection = browser.find_element_by_css_selector(category_selector)
            category_text = category_selection.text
            category_selection.click()

        else:
            time.sleep(0.75)
            category_selector = "div#hmenu-content > ul.hmenu-visible > li:nth-child({}) > a".format(category)
            category_selection = browser.find_element_by_css_selector(category_selector)
            category_text=category_selection.text
            WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, category_selector))).click()

        time.sleep(1)
        sub_category_selector = "div#hmenu-content > ul.hmenu-visible > li:nth-child({}) > a".format(sub_category)
        sub_category_selection = browser.find_element_by_css_selector(sub_category_selector)
        sub_text=sub_category_selection.text
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, sub_category_selector))).click()

        if sub_category == 3:
            cat_dict = {"Category":category_text}
            cat_list = []
            cat_list.append(cat_dict)
            df = pd.DataFrame(cat_list)
            df.to_csv("scraping/category.csv",index=False,header=False,mode="a")
        sub_list =[]
        dict_sub = {"SubCategory": sub_text, "CategoryId": category - 6}
        sub_list.append(dict_sub)
        df2 = pd.DataFrame(sub_list)
        df2.to_csv("scraping/subcategory.csv",index=False,header=False,mode="a")

        product_list = get_products(browser, category-6, sub_category-2)
        print(product_list)
        product_dict_list = []
        for product in product_list:
            product_dict_list.append({"Name":product.name,"Price":product.price,"Stock":product.stock,"Category":product.category,"SubCategory":product.subcategory,"ImagePath":product.image})
        df = pd.DataFrame(product_dict_list)
        df.to_csv("scraping/product.csv",index=False,header=False,mode="a")
    except selenium.common.exceptions.NoSuchElementException:
        try:
            WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#hmenu-canvas-background > div"))).click()
        except selenium.common.exceptions.TimeoutException:
            pass
        return False
    return True


