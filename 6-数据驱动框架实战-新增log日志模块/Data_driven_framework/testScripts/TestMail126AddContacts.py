#encoding = utf-8
from testScripts.TestMail126 import *
from appModules.AddContactPersonAction import AddContactPersonAcition
import time
from config.VarConfig import *
from util.ParseExcel import ParseExcel
from util.log import *
pe = ParseExcel()
pe.loadWorkBook(excelPath)
sheet = pe.getSheetByName(sheetName)
log = Log()
def test126MailClickMailList(driver):
    AddContactPersonAcition.clickMailList(driver)
    log.info("点击通讯录")

def test126MailAddContacts(driver,contactName,contactEmail,contactPhone):
    try:
        AddContactPersonAcition.add(driver,contactName,contactEmail,contactPhone)
        driver.implicitly_wait(10)
    except Exception as e:
        raise e
def test126Mail():
    try:
        driver = testMailLogin()
        assert u"未读邮件" in driver.page_source
        pe.writeCell(pe.getSheetByName(sheetName_Account),"登录成功",2,6)
        log.info("断言页面关键字“未读邮件”成功")
        test126MailClickMailList(driver)
        j = int(pe.getRowsNum(sheet))
        i = 2
        if j <= 1:
            # print(excelPath + "_______表名：" + sheetName + "_______测试数据为空")
            log.info(excelPath + "_______表名：" + sheetName + "_______测试数据为空")
        else:
            while i <= j:
                if str(pe.getCellOfValue(sheet, i, 8)) == 'y':
                    contactName = pe.getCellOfValue(sheet, i, contacts_PersonName)
                    contactEmail = pe.getCellOfValue(sheet, i, contacts_PersonMail)
                    contactPhone = pe.getCellOfValue(sheet, i, contacts_PersonPhone)
                    test126MailAddContacts(driver, contactName, contactEmail, contactPhone)
                    # print("新建一条联系人成功...")
                    log.info("新建一条联系人成功...")
                    pe.writeCell(sheet, "测试通过", i, 10)
                    pe.writeCell(sheet, pe.getCurrentTime(), i, 9)
                else:
                    # print(excelPath + "_______表名：" + sheetName + "_______是否执行标志为n，测试数据跳过执行")
                    log.info(excelPath + "_______表名：" + sheetName + "_______是否执行标志为n，测试数据跳过执行")
                    pe.writeCell(sheet, "N/A", i, 10)
                    pe.writeCell(sheet, pe.getCurrentTime(), i, 9)
                i = i + 1
        driver.quit()
        # print("脚本加载完毕...")
        log.info("脚本加载完毕...")
    except Exception as e:
        # print("未找到未读邮件,登录失败，正在退出...")
        log.info("未找到未读邮件,登录失败，正在退出...")
        pe.writeCell(pe.getSheetByName(sheetName_Account),"登录失败",2,6)
        driver.quit()



if __name__ == '__main__':
    test126Mail()