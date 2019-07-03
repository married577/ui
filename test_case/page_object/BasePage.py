from time import sleep


class Page():
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'http://119.3.49.246/dist/#/login'

    def _open(self, url):
        url_ = self.base_url+url
        # # print("当前页面网址为： %s" % url_)
        # self.driver.maximize_window()
        # self.driver.get(url_)
        # sleep(2)

    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)
