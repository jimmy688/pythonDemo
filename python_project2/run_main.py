import requests
from interfaces.recruitSystem import Recruitsys
import unittest
import os
import HTMLTestRunner
from MyUtils.emailUtils import sendEmail

def addTests():
    basepath=os.path.realpath(os.path.dirname(__file__))
    case_dir=os.path.join(basepath,"cases")
    suite=unittest.defaultTestLoader.discover(
        start_dir=case_dir,
        pattern='test*.py',
        top_level_dir=None
    )
    return suite


if __name__=='__main__':
    #进行测试并生成报告
    filepath='E:/python_projects/python_project2/report/day927_01.html'
    fp=open(filepath,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='测试报告',description='我的html测试报告')
    runner.run(addTests())

    #发送邮件
    sender='974643517@qq.com'
    receivers=['974643517@qq.com']  #,'303318603@qq.com'
    sendEmail("smtp.qq.com",465,sender,receivers,"gofyiuzkjzlzbdic",
              ['E:/python_projects/python_project2/report/day927_01.html'],['day927_01.html'])
