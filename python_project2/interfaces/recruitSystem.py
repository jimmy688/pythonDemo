import requests
import json

class Recruitsys():
    s=None
    def __init__(self,s):
        self.s=s
    def login(self, username, password):
        url = 'http://192.168.239.137:8080/recruit.students/login/in'
        pwd = {
            'account': username,
            'pwd': password
        }
        r = self.s.get(url=url, params=pwd)
        return r

    def addSchool(self,schoolName,typeid,canrecruit,remark):

        url='http://192.168.239.137:8080/recruit.students/school/manage/addSchoolInfo'
        payload={
            "schoolName": schoolName,
            "listSchoolType%5B0%5D.id": typeid,
            "canRecruit": canrecruit,
            "remark": remark
        }
        r=self.s.post(url,data=payload)
        return r

    def enableOrDisable(self,id6,sid3,isable):
        url='http://192.168.239.137:8080/recruit.students/school/manage/enableOrDisableSchool'
        payload=[{"id":id6,"disable":isable,"schoolId":sid3}]
        r=self.s.post(url,json=payload)
        return r

    def setStudentRecruitTime(self,id,startTime,endTime,isSRtime):
        url='http://192.168.239.137:8080/recruit.students/school/manage/setStudentRecruitTime'

        #对字符串格式化时注意下双引号，比如下面一行代码%s两端的双引号，不能去掉，否则会报错
        payload='[{"id":%d,"recruitStartTime":"%s","recruitEndTime":"%s","isStudentRecruitTime":%s}]'%(id,startTime,endTime,isSRtime)
        # print(payload)
        r=self.s.post(url,json=json.loads(payload))
        return r

if __name__=='__main__':
    import requests
    recruitsys=Recruitsys(requests.Session())

