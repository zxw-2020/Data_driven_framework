#encoding = utf-8
from testScripts.TestMail126 import *
from appModules.AddContactPersonAction import AddContactPersonAcition
import time
from config.VarConfig import *
from util.ParseExcel import ParseExcel
pe = ParseExcel()
pe.loadWorkBook(excelPath)
sheet = pe.getSheetByName(sheetName)
def test126MailAddContacts(driver,contactName,contactEmail,contactPhone):
    try:
        AddContactPersonAcition.add(driver,contactName,contactEmail,contactPhone)
        driver.implicitly_wait(10)
    except Exception as e:
        raise e
if __name__ == '__main__':
    driver = testMailLogin()
    j=int(pe.getRowsNum(sheet))
    i=2
    while i<j:
        contactName=pe.getCellOfValue(sheet,i,contacts_PersonName)
        contactEmail=pe.getCellOfValue(sheet,i,contacts_PersonMail)
        contactPhone=pe.getCellOfValue(sheet,i,contacts_PersonPhone)
        i=i+1
        test126MailAddContacts(driver,contactName,contactEmail,contactPhone)
    driver.quit()
    print("登录成功")