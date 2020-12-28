#encoding = utf-8
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
import time
from appModules.LoginAction import LoginAction

def testMailLogin():
    try:
        driver = webdriver.Firefox(executable_path="C:\\webdriver\geckodriver.exe")
        driver.get("http://mail.126.com")
        driver.implicitly_wait(30)
        driver.maximize_window()
        time.sleep(5)
        LoginAction.login(driver,"zxw18050403070","18050403070zxw")
        time.sleep(10)
        assert u"未读邮件" in driver.page_source
    except Exception as e:
        raise e
    finally:
        driver.quit()
if __name__ == '__main__':
    testMailLogin()
    print("登录成功")