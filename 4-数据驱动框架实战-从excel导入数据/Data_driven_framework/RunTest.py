#encoding = utf-8
from testScripts.TestMail126AddContacts import *
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