#encoding = utf-8
from util.ObjectMap import *
from util.ParseConfigurationFile import ParserConfigFile

class HomePage(object):
    def __init__(self,driver):
        self.driver=driver
        self.parseCF=ParserConfigFile()
    def addressLink(self):
        try:
            locateType,locatorExpression=self.parseCF.getOptionValue("126mail_homepage","homePage.addressbook").split(">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

