import unittest
from driver.driver import *
from time import sleep
from selenium import webdriver


class StartEnd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


