from MyUtils.mysqlUtils import MysqlUtils
import unittest
from interfaces.recruitSystem import Recruitsys
import requests
import ddt

s=requests.session()
recruitsys=Recruitsys(s)
recruitsys.login('admin','660B8D2D5359FF6F94F8D3345698F88C')

mu = MysqlUtils()
sid = mu.get_data('SELECT f_school_id FROM `t_login_account` ' \
                   'order by f_school_id desc limit 1;')[0]     #从数据库中拿数据
# print(type(sid))
data=[
    {"id": sid, "startTime":"null","endTime":"null","isSRtime":"0","expect":1},
    {"id": sid, "startTime": "2020-06-05", "endTime": "2020-07-09", "isSRtime": "1","expect":1},
    {"id": sid, "startTime": "2020/06-05", "endTime": "2020-07-09", "isSRtime": "1","status":10001},
    {"id": sid, "startTime": "2020-06-05", "endTime": "2020-07-35", "isSRtime": "1","status":10001},
    {"id": sid, "startTime": "2020-06-05", "endTime": "2020-07-09", "isSRtime": "0","expect":1},
    {"id": sid, "startTime": "null", "endTime": "null", "isSRtime": "0","status":10001}
]

@ddt.ddt
class SetStudentRecruitTime(unittest.TestCase):
    def setUp(self) -> None:
        pass

    @ddt.data(*data)
    def test_01(self,testdata):
        r=recruitsys.setStudentRecruitTime(testdata["id"],testdata["startTime"],testdata["endTime"],testdata["isSRtime"])
        print(r.text)
        try:
            result=r.json()['code']
            print("设置时间成功了")
        except Exception:
            result=r.json()['status']
            print("设置时间失败了")


    def tearDown(self) -> None:
        s.close()



if __name__=='__main__':
    unittest.main()