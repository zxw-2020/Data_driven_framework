#encoding = utf-8
from testScripts.TestMail126 import *
from testScripts.TestMail126AddContacts import *
if __name__ == '__main__':
    driver = testMailLogin()
    test126MailAddContacts(driver)
    driver.quit()
    print("登录成功")