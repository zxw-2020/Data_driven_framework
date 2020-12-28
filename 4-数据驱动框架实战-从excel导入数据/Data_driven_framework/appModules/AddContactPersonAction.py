#encoding = utf-8
from pageObjects.HomePage import HomePage
from pageObjects.AddressBookPage import AddressBookPage
import traceback
import time
class AddContactPersonAcition(object):
    def __init__(self):
        print("add contact person")
    @staticmethod
    def add(driver,contactName,contactEmail,contactPhone):
        try:
            print("add contact person")
            hp=HomePage(driver)
            hp.addressLink().click()
            time.sleep(2)
            ap=AddressBookPage(driver)
            ap.new_contact().click()
            time.sleep(2)
            ap.add_name().send_keys(contactName)
            ap.add_mail().send_keys(contactEmail)
            ap.add_phone().send_keys(contactPhone)
            ap.add_confirm().click()
            time.sleep(2)
        except Exception as e:
            raise e