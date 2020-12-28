#encoding =utf-8
import os

#获取当前文件所在目录的绝对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#获取存放页面元素定位表达式文件的绝对路径

pageElementLocatorPath=parentDirPath+ u"\\config\\PageElementLocator.ini"

FirefoxPath="C:\\webdriver\geckodriver.exe"
log_path = parentDirPath+u"\\log\\"
testAddress="http://mail.126.com"

excelPath = parentDirPath+u"\\testData\\126邮箱联系人.xlsx"
sheetName = "联系人"
sheetName_Account="126账号"
account_name=2
account_pwd=3

contacts_PersonName=2
contacts_PersonMail=3
contacts_PersonPhone=5
