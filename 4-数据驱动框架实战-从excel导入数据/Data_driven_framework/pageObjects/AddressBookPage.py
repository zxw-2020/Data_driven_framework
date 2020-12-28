#encoding = utf-8
from util.ObjectMap import *
from util.ParseConfigurationFile import ParserConfigFile

class AddressBookPage(object):
    def __init__(self,driver):
        self.driver=driver
        self.parseCF=ParserConfigFile()
    def new_contact(self):
        try:
            locateType,locatorExpression=self.parseCF.getOptionValue("126mail_addpage","addpage.new_contact").split(">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e
    def add_name(self):
        try:
            locateType,locatorExpression=self.parseCF.getOptionValue("126mail_addpage","addpage.name").split(">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e
    def add_mail(self):
        try:
            locateType,locatorExpression=self.parseCF.getOptionValue("126mail_addpage","addpage.mail").split(">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e
    def add_phone(self):
        try:
            locateType,locatorExpression=self.parseCF.getOptionValue("126mail_addpage","addpage.phone").split(">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e
    def add_confirm(self):
        try:
            locateType,locatorExpression=self.parseCF.getOptionValue("126mail_addpage","addpage.confirm").split(">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e