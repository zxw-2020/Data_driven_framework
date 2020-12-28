#encoding = utf-8
from selenium import webdriver
import time
from appModules.LoginAction import LoginAction

def testMailLogin():
    try:
        driver = webdriver.Firefox(executable_path="C:\\webdriver\geckodriver.exe")
        driver.get("http://mail.126.com")
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.implicitly_wait(10)
        LoginAction.login(driver,"zxw18050403070","18050403070zxw")
        time.sleep(10)
        assert u"未读邮件" in driver.page_source
        return driver
    except Exception as e:
        raise e
if __name__ == '__main__':
    driver=testMailLogin()
    driver.quit()
    print("登录成功")