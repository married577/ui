import unittest
from test_case.model import function, myunit
from test_case.page_object.LoginPage import *
from time import sleep
import csv
from logger import Log
from driver.driver import *
log = Log()


class LoginTest(myunit.StartEnd):
    my_file = csv.reader(open('f:/secret.csv', 'r'))
    list = []
    for data in my_file:
        list.append(data)

    # @unittest.skip('无条件跳过用例')
    @unittest.skipUnless(1 < 2, "左边小于右边，用例才会执行")
    def test_login(self):

        po = LoginPage(self.driver)
        po.Login_action(self.list[0][0], self.list[0][1], '')
        sleep(2)
        log.info('--登陆成功--')

    def test_open(self):

        po = LoginPage(self.driver)
        po.Open_action('', '')
        sleep(2)


if __name__ == '__main__':
    unittest.main()
