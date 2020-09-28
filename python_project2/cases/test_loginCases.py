import requests
import unittest
import re
import ddt
from interfaces.recruitSystem import Recruitsys

s=requests.session()
recruitsys=Recruitsys(s)


data=[
    {"account":"admin","psw":"660B8D2D5359FF6F94F8D3345698F88C","expect":"退出登录"},
    {"account":"admin","psw":"660B8D2D5359FF6F94F8D3345698F88C","expect":""},
    {"account":"admin","psw":"660B8D2D5359FF6F94F8D3345698F88C","expect":""},
]

@ddt.ddt
class LoginCases(unittest.TestCase):

    def setUp(self) -> None:
        pass

    @ddt.data(*data)
    def test_01(self,testdata):   #必须以test开头
        r=recruitsys.login(testdata['account'],testdata['psw'])
        # print(r.text)
        try:
            result=re.findall('退出登录',r.text)[0]
        except Exception:
            result=''
        self.assertTrue(result==testdata['expect'])

    def tearDown(self) -> None:
        s.close()

if __name__=='__main__':
    unittest.main()
