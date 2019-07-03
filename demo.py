from selenium import webdriver
from logger import Log
import unittest
import csv
from time import sleep
log = Log()


class login(unittest.TestCase):
    my_file = csv.reader(open('f:/secret.csv', 'r'))
    list = []
    for data in my_file:
        list.append(data)

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://119.3.49.246/dist/#/login")
        cls.driver.maximize_window()
        log.info('--测试用例开始--')
        sleep(5)

    def test_case1(self):
        log.info('--输入账号--')
        self.driver.find_element_by_xpath('//*[@id="app"]/form/div[1]/div/div/input').send_keys(self.list[0][0])
        sleep(1)
        log.info('--输入密码--')
        self.driver.find_element_by_xpath('//*[@id="app"]/form/div[2]/div/div/input').send_keys(self.list[0][1])
        sleep(1)
        log.info('--点击登录--')
        self.driver.find_element_by_xpath('//*[@id="app"]/form/div[3]/div/button').click()
        sleep(3)
        t = self.driver.title
        log.error(u'获取title内容：%s' %t)
        if t == '豪爽钱包后台':
            print('title获取成功')
        else:
            print('title获取失败')

    def testcase2(self):
        log.info('--打开渠道管理--')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/aside/ul/li[2]/div').click()
        sleep(1)
        log.info('--打开渠道后台--')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/aside/ul/li[2]/ul/li[3]').click()
        sleep(2)
        log.info('--点击选择渠道按钮--')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/section/div[1]/div[1]/input')\
            .click()
        sleep(2)
        log.info('--选择渠道--')
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[4]').click()
        sleep(2)

    @classmethod
    def tearDownClass(cls):
        log.info('--测试用例结束--')
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(login('test_case1'))
    suite.addTest(login('test_case2'))

    runner = unittest.TextTestRunner
    runner.run(suite)








