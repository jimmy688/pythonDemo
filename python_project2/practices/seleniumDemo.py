from selenium import webdriver
import time

browser = webdriver.Chrome()
res = browser.get('http://www.baidu.com')
browser.quit()


def SeDemo():
    options=webdriver.ChromeOptions()
    options.binary_location='E:\install\python_install\chromedriver.exe'

    print(res.text)

SeDemo()
