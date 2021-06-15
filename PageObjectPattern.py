from selenium import webdriver
from selenium.webdriver import Firefox
from abc import ABC
from selenium.webdriver.common.by import By

class PageElement(ABC):
    def __init__(self, webdriver):
        self.webdriver = webdriver

class Login(PageElement):
       UserName = (By.ID, 'userName')
       Password = (By.ID, 'password')
       BotaoLogin = (By.ID, 'login')
       ##BotaoNewUser = (By.ID, 'newUser')

       def create_Login(self, UserName, Password):
           self.webdriver.find_element(*self.UserName).send_keys(UserName)
           self.webdriver.find_element(*self.Password).send_keys(Password)
           self.webdriver.find_element(*self.BotaoLogin).click()

webdriver = Firefox()

url = 'https://demoqa.com/login'

webdriver.get(url)

login_page = Login (webdriver)

login_page.create_Login(
    UserName='LaisFloriano',
    Password='#Lais1022'
)
