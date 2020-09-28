import requests
import unittest
import re
import ddt
import random
from interfaces.recruitSystem import Recruitsys
from MyUtils.otherUtils import generateName

s=requests.session()
recruitsys=Recruitsys(s)

recruitsys.login("admin","660B8D2D5359FF6F94F8D3345698F88C")

data=[
    {"schoolName":generateName(),"typeid":"1","canrecruit":1,"remark":None},
    {"schoolName":generateName(),"typeid":"2","canrecruit":1,"remark":"abc"},
    {"schoolName":generateName(),"typeid":"3","canrecruit":1,"remark":None},
    {"schoolName":generateName(),"typeid":"1","canrecruit":0,"remark":None},
    {"schoolName":None,"typeid":"1","canrecruit":1,"remark":None},
]

@ddt.ddt
class AddSchoolCases(unittest.TestCase):
    #这里不能加def  __init__(self)，会报错，还不知什么原因

    def setUp(self) -> None:
        pass

    @ddt.data(*data)
    def test_01(self,testdata):
        r=recruitsys.addSchool(testdata['schoolName'],testdata['typeid'],
                               testdata['canrecruit'],testdata['remark'])
        try:
            result=r.json()['code']
            self.assertTrue(result == 1)
        except Exception:
            result=r.json()['status']
            self.assertTrue(result == 10001)
        # print(result)



    def tearDown(self) -> None:
        s.close()


if __name__=='__main__':
    unittest.main()

