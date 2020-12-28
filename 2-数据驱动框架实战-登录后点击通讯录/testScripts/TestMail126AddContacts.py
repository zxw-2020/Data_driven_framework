#encoding = utf-8
from testScripts.TestMail126 import *
from appModules.AddContactPersonAction import AddContactPersonAcition
import time
def test126MailAddContacts(driver):
    try:
        AddContactPersonAcition.add(driver)
        time.sleep(10)
    except Exception as e:
        raise e
if __name__ == '__main__':
    driver = testMailLogin()
    test126MailAddContacts(driver)
    driver.quit()
    print("登录成功")