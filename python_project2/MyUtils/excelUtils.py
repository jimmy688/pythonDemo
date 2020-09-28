# coding=utf-8

import xlrd

# data=[
#     {'name': 'Jimmy', 'age': 18.0, 'sex': 'male'},
#     {'name': 'krystal', 'age': 15.0, 'sex': 'female'},
#     {'name': 'Jack', 'age': 23.0, 'sex': 'male'}
# ]

class ExcelUtil():
    def __init__(self,excelPath,sheetName='Sheet1'):
        self.book=xlrd.open_workbook(excelPath)
        self.sheet_t=self.book.sheet_by_name(sheetName)
        #获取第一行作为key值
        self.keys=self.sheet_t.row_values(0)
        #获取总行数
        self.rowNum=self.sheet_t.nrows
        #获取总列数
        self.colNum=self.sheet_t.ncols

    def dict_data(self):
        if self.rowNum<2:
            print("总行数小于2")
        else:
            r=[]
            j=1
            for i in range(self.rowNum-1):
                s={}
                #从第二行取对应的values值
                values=self.sheet_t.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]]=values[x]   #写入字典中
                r.append(s)  #将字典追加到列表中
                j+=1
            return r

if __name__=='__main__':
    excelPath="../source/test.xlsx"
    sheetName="Sheet1"
    myexcel=ExcelUtil(excelPath,sheetName=sheetName)
    print(myexcel.dict_data())