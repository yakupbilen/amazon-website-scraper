from scraping.amazon_scraping import open_menu
from selenium import webdriver
import time

if __name__ == "__main__":
    browser = webdriver.Chrome("scraping/chromedriver.exe")
    browser.maximize_window()
    browser.get("https://www.amazon.com")
    time.sleep(1)

    for i in range(7,29):
        j = 3
        while open_menu(browser, i, j):
            j += 1

    browser.close()