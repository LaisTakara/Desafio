#Crie ao menos 1 teste que valide o comportamento dos componentes da tela e
# efetivação do fluxo “Register to Book Store”
from selenium.webdriver import Firefox
from time import sleep

url = 'https://demoqa.com/login'

firefox = Firefox ()

firefox.get(url)

sleep(3)

firefox.maximize_window()

##LOGIN##
loginInicio = firefox.find_element_by_xpath('//*[@id="login"]').click()
sleep(3)

def loginSucesso(browser, userName, password):

    firefox.find_element_by_id('userName').send_keys(userName)
    firefox.find_element_by_id('password').send_keys(password)
    firefox.find_element_by_xpath('//*[@id="login"]').click()


loginSucesso(
   firefox,
   'LaisFloriano',
   '#Lais1022'

)

#firefox.quit()
