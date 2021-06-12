from selenium.webdriver import Firefox
from time import sleep

url = 'https://demoqa.com/books'

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

sleep(3)

def consultaLivro(browser, searchBox):

    firefox.find_element_by_id('searchBox').send_keys(searchBox)
    sleep(5)
    firefox.find_element_by_id('basic-addon2').click()

consultaLivro(
    firefox,
    'JavaScript',
)

selecionaLivro = firefox.find_element_by_class_name('mr-2').click()
AdicionarColecao = firefox.find_element_by_css_selector('div.text-right:nth-child(2) > button').click()



#firefox.quit()
