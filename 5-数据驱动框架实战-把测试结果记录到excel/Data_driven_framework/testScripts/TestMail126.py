#encoding = utf-8
from selenium import webdriver
import time
from appModules.LoginAction import LoginAction
from config.VarConfig import *
from util.ParseExcel import ParseExcel
pe = ParseExcel()
pe.loadWorkBook(excelPath)
sheet = pe.getSheetByName(sheetName_Account)

def testMailLogin():
    try:
        driver = webdriver.Firefox(executable_path=FirefoxPath)
        driver.get(testAddress)
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.implicitly_wait(10)
        j = int(pe.getRowsNum(sheet))
        i = 2
        if j <= 1:
            print(excelPath + "_______表名：" + sheetName_Account + "_______测试数据为空")
        else:
            while i <= j:
                if str(pe.getCellOfValue(sheet, i, 5))=='y':
                    if pe.getCellOfValue(sheet, i, 1)==1 :
                        Account = pe.getCellOfValue(sheet, i, account_name)
                        password = pe.getCellOfValue(sheet, i, account_pwd)
                        LoginAction.login(driver, Account, password)
                else:
                    print(excelPath + "_______表名：" + sheetName_Account + "_______是否执行标志为n，测试数据不可执行")
                i = i + 1
        time.sleep(10)
    except Exception as e:
        raise e
    finally:
        return driver
if __name__ == '__main__':
    driver=testMailLogin()
    driver.quit()
    print("脚本加载完毕...")