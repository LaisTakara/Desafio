from selenium.webdriver.common.by import By

class Login:
   def __init__(self, webdriver):
    self.UserName = (By.ID, 'userName')
    self.Password = (By.ID, 'password')
    self.BotaoLogin = (By.ID, 'login')
    self.BotaoNewUser = (By.ID, 'newUser')
       
    self.webdriver = webdriver

    def create_Login(self, UserName, Password, BotaoLogin, BotaoNewUser):
        self.webdriver.find_element(*self.UserName).send_keys(UserName)
        self.webdriver.find_element(*self.Password).send_keys(Password)
        self.webdriver.find_element(*self.BotaoLogin).click()
    
    ##self.webdriver.findelement(*self.BotaoNewUser).send_keys(BotaoLogin)


    from selenium.webdriver import Firefox 

    webdriver = Firefox()

    url = 'https://demoqa.com/login'

    webdriver.get(url)

    login_page = Login (webdriver)

    login_page.create_Login(
        'LaisFloriano',
        '#Lais1022'
    )
