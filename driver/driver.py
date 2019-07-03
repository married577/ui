from selenium import webdriver
from time import sleep


def browser():
    driver = webdriver.Chrome()

    driver.get("http://119.3.49.246/dist/#/login")
    driver.implicitly_wait(3)
    driver.maximize_window()
    sleep(2)

    return driver


if __name__ == "__main__":
    browser()
















