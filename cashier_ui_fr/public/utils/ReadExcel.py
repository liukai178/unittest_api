#coding = utf-8
'''
用于读取excel文件的工具
'''
import xlrd
import os
# 导入data的绝对路径
from config.globalconfig import data_path
class ReadExcel:
    #构造函数中已经找到对应的sheet
    def __init__(self,filename,sheetname):
        #filename参数为excel文件名
        #datapath为excel文件的绝对路径和名称
        datapath = os.path.join(data_path,filename)
        #读取excel文件并且生成一个对象
        self.workbook = xlrd.open_workbook(datapath)
        #找到对应Sheet
        self.sheetName = self.workbook.sheet_by_name(sheetname)

    def read_excel(self,rownum,colnum):
        #找到相应sheet中具体行列对应的值!
        value  = self.sheetName.cell(rownum,colnum).value
        #返回这个值
        return value



