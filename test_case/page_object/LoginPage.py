from test_case.page_object.BasePage import *
from selenium.webdriver.common.by import By


class LoginPage(Page):
    url = '/'

    username_loc = (By.XPATH, '//*[@id="app"]/form/div[1]/div/div/input')
    password_loc = (By.XPATH, '//*[@id="app"]/form/div[2]/div/div/input')
    submit_loc = (By.XPATH, '//*[@id="app"]/form/div[3]/div/button')

    manage_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/aside/ul/li[2]/div')
    houtai_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/aside/ul/li[2]/ul/li[3]')
    qudaoall_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/section/div[1]/div[1]/input')
    qudao_loc = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[4]')

    def type_username(self, username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)
        sleep(2)

    def type_password(self, password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)
        sleep(2)

    def type_submit(self, submit):
        self.find_element(*self.submit_loc).click()
        sleep(2)

    def type_manage(self, manage):
        self.find_element(*self.manage_loc).click()
        sleep(2)

    def type_houtai(self, houtai):
        self.find_element(*self.houtai_loc).click()
        sleep(2)

    def type_qudaoall(self, qudaoall):
        self.find_element(*self.qudaoall_loc).click()
        sleep(2)

    def type_qudao(self, qudao):
        self.find_element(*self.qudao_loc).click()
        sleep(2)

    def Login_action(self, username, password, submit):
        self.open()
        self.type_username(username)
        self.type_password(password)
        self.type_submit(submit)

    def Open_action(self, manage, houtai):
        self.open()
        self.type_manage(manage)
        self.type_houtai(houtai)

    def Choose_action(self, qudaoall, qudao):
        self.open()
        self.type_qudaoall(qudaoall)
        self.type_qudao(qudao)

