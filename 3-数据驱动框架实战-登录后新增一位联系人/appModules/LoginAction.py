#encoding=utf-8
from pageObjects.LoginPage import LoginPage

class LoginAction(object):
    def __init__(self):
        print("login...")
    @staticmethod
    def login(driver,username,password):
        try:
            loginPage=LoginPage(driver)
            loginPage.switchAccountLogin().click()
            driver.switch_to.frame(loginPage.switchToFrame())
            loginPage.userNmaeObj().send_keys(username)
            loginPage.passwordObj().send_keys(password)
            loginPage.loginButton().click()
            loginPage.switchToDefaultFrame()
        except Exception as e:
            raise e

if __name__=='__main__':
    from selenium import webdriver
    import time
    driver = webdriver.Firefox(executable_path="C:\\webdriver\geckodriver.exe")
    driver.get("http://mail.126.com")
    time.sleep(5)
    LoginAction.login(driver,username="zxw18050403070",password="18050403070zxw")
    time.sleep(5)
    driver.quit()