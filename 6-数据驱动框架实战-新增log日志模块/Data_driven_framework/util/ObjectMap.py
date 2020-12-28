#encoding = utf-8
from selenium.webdriver.support.ui import WebDriverWait

#获取单个页面元素
def getElement(driver,locateType,locatorExpression):
    try:
        element=WebDriverWait(driver,30).until(lambda x:x.find_element(by=locateType,value=locatorExpression))
        return element
    except Exception as e:
        raise e
#获取多个相同页面元素对象，以list返回
def getElements(driver,locateType,locatorExpression):
    try:
        elements=WebDriverWait(driver,30).until(lambda x:x.find_elements(by=locateType,value=locatorExpression))
        return elements
    except Exception as e:
        raise e


#测试上面代码
if __name__=='__main__':
    from selenium import webdriver
    driver=webdriver.Firefox(executable_path="C:\\webdriver\geckodriver.exe")
    driver.get("http://www.baidu.com")
    searchBox =getElement(driver,"id","kw")
    print(searchBox.tag_name)
    searchBox =getElements(driver,"id","kw")
    print(len(searchBox))
    alist=getElements(driver,"tag name","a")
    print(len(alist))
    driver.quit()