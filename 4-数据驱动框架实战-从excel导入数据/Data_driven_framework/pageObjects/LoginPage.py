#encoding = utf-8
from util.ObjectMap import *
from util.ParseConfigurationFile import ParserConfigFile

class LoginPage(object):
    def __init__(self,driver):
        self.driver =driver
        self.parseCF=ParserConfigFile()
        self.loginOptions =self.parseCF.getItemsSection("126mail_login")
    def switchToFrame(self):
        try:
            locateType,locatorExpression=self.loginOptions["loginPage.frame".lower()].split(">")
            elementObj =getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e
    def switchToDefaultFrame(self):
        self.driver.switch_to.default_content()

    def userNmaeObj(self):
        try:
            locateType,locatorExpression=self.loginOptions["loginPage.username".lower()].split(">")
            elementObj =getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def passwordObj(self):
        try:
            locateType,locatorExpression=self.loginOptions["loginPage.password".lower()].split(">")
            elementObj =getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def loginButton(self):
        try:
            locateType,locatorExpression=self.loginOptions["loginPage.loginbutton".lower()].split(">")
            elementObj =getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e
    def switchAccountLogin(self):
        try:
            locateType,locatorExpression=self.loginOptions["loginPage.switchAccountLogin".lower()].split(">")
            elementObj =getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

if __name__=='__main__':
    from selenium import webdriver
    driver=webdriver.Firefox(executable_path="C:\\webdriver\geckodriver.exe")
    import time
    driver.get("http://mail.126.com")
    time.sleep(5)
    login=LoginPage(driver)
    login.switchAccountLogin().click()
    driver.switch_to.frame(login.switchToFrame())
    login.userNmaeObj().send_keys("xxx")
    time.sleep(5)
    login.passwordObj().send_keys("xxx")
    time.sleep(5)
    login.loginButton().click()
    time.sleep(5)
    login.switchToDefaultFrame()
    driver.quit()
