#encoding = utf-8
from pageObjects.HomePage import HomePage
from pageObjects.AddressBookPage import AddressBookPage
import traceback
import time
class AddContactPersonAcition(object):
    def __init__(self):
        print("add contact person")
    @staticmethod
    def add(driver):
        try:
            print("add contact person")
            hp=HomePage(driver)
            hp.addressLink().click()
            time.sleep(3)
            ap=AddressBookPage(driver)
            ap.new_contact().click()
            time.sleep(3)
            ap.add_name().send_keys("张三")
            time.sleep(3)
            ap.add_mail().send_keys("12346@qq.com")
            time.sleep(3)
            ap.add_phone().send_keys("18050403999")
            time.sleep(3)
            ap.add_confirm().click()
        except Exception as e:
            raise e