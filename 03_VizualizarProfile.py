from selenium.webdriver import Firefox
from time import sleep

url = 'https://demoqa.com/login'

firefox = Firefox ()

firefox.get(url)

sleep(3)

def loginSucesso(browser, userName, password):

    firefox.find_element_by_id('userName').send_keys(userName)
    firefox.find_element_by_id('password').send_keys(password)
    sleep(5)
    firefox.find_element_by_id('login').click()

loginSucesso(
    firefox,
    'LaisFloriano',
    '#Lais1022'
)


## Validação de usuário logado + print de tela

#userName = firefox.find_element_by_css_selector('[#userName-value="LaisFloriano"]')

# def validacaoLogin(browser,userName):
#
#     firefox.find_element_by_xpath('//*[@id="userName-value"]')
