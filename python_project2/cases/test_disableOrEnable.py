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

addSchool_r=recruitsys.addSchool(generateName(),"1",1,None)
id3=addSchool_r.json()['data']['id']
schoolid6=addSchool_r.json()['data']['laccount']

data=[
    {"disable":1,"id":schoolid6,"schoolid":id3,"expect":1},
    {"disable":0,"id":schoolid6,"schoolid":id3,"expect":1}
]

@ddt.ddt
class DisableOrEnable(unittest.TestCase):

    def setUp(self) -> None:
        pass

    @ddt.data(*data)
    def test_01(self,testdata):
        r=recruitsys.enableOrDisable(testdata['id'],testdata['schoolid'],
                                     testdata['disable'])
        result=r.json()['code']
        self.assertTrue(result==testdata['expect'])

    def tearDown(self) -> None:
        s.close()

if __name__=='__main__':
    unittest.main()