# 读取excel，读取用例内容，写入测试结果

import openpyxl
import os
from common.handlepath import *

case_file= os.path.join(DATADIR,"apicase.xlsx")
#excel文件目录
# print(case_file)
class ReadExcel(object):
    def __init__(self,filename,sheetname):
        self.filename = filename
        self.sheetname = sheetname

    def open(self):
        #封装一个打开excel表格的方法
        self.wb = openpyxl.load_workbook(self.filename)
        self.sh = self.wb[self.sheetname]


    def read_data(self):
        #打开工作簿的方法
        self.open()
        #取到每一行数据放入到元组当中
        datas = list(self.sh.rows)
        # print(datas)
        title = [i.value for i in datas[0]]
        #收集第一行的每一个数据（表头，以后的键）
        # print(title)

        cases=[]
        #定义一个空列表用来接收所有的接口用例参数
        for i in datas[1:]:
        #切片法：从第二行开始循环,搜集除了第一行外的所有数据
            values = [c.value for c in i]
            #逐个取每行的数据
            # print(values)
            case = dict(zip(title,values))
            #通过子zip函数把title和values用键值对的形式拼接起来
            # print(case)
            cases.append(case)
            #把case的值添加到cases列表中
            # print(cases)

        return cases

    def write_data(self,row,column,value=None):
        #定义一个数据回写的方法（写入测试结果）
        self.open()
        #打开文件
        self.sh.cell(row,column,value)
        #写入（行，列，值）
        self.wb.save(self.filename)
        #保存文件

if __name__ == '__main__':
    r = ReadExcel(case_file,"login")
    print(r.read_data())
    # r.write_data(2,8,"假装通过")




