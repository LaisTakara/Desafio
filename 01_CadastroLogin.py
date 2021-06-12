from selenium.webdriver import Firefox
from time import sleep

url = 'https://demoqa.com/books'

firefox = Firefox ()

firefox.get(url)

sleep(3)

##LOGIN##
loginInicio = firefox.find_element_by_xpath('//*[@id="login"]').click()
sleep(3)

newUser = firefox.find_element_by_id ('newUser').click()
sleep(3)

def cadSucesso(browser, firstname, lastname, userName, password):

    firefox.find_element_by_id('firstname').send_keys(firstname)
    firefox.find_element_by_id('lastname').send_keys(lastname)
    firefox.find_element_by_id('userName').send_keys(userName)
    firefox.find_element_by_id('password').send_keys(password)
    firefox.find_element_by_class_name('recaptcha-checkbox-border').click()
    sleep(5)
    firefox.find_element_by_id('register').click()

cadSucesso(
   firefox,
   'Lais',
   'Floriano',
   'LaisFloriano',
   '#Lais1022'

)

firefox.quit()