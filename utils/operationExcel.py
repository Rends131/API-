import xlrd
from common.public import filePath
from utils.operationYaml import OperationYaml
from common.public import *

class ExcelValues:
    caseID=0 #第一行
    des=1 #第二行 描述
    url=2 #第三行 地址
    method= 3 #第四行 请求方法
    data=4 #第五行 参数
    expect=5 #第六航 期望结果

    @property
    def getCaseID(self):
        return self.caseID

    @property
    def description(self):
        return self.des

    @property
    def getUrl(self):
        return self.url

    @property
    def getMethod(self):
        return self.method

    @property
    def getData(self):
        return self.data

    @property
    def getExpect(self):
        return self.expect

class OpenreationExcel(OperationYaml):
    def getSheet(self):
        book=xlrd.open_workbook(filePath("data","books.xlsx"))
        return book.sheet_by_index(0)

    @property
    def getRows(self):
        """获取总行数"""
        return self.getSheet().nrows

    @property
    def getCols(self):
        """获取总列数"""
        return self.getSheet().ncols

    def getValue(self,row,col):
        """获取对应的内容"""
        return self.getSheet().cell_value(row,col)

    def getCaseID(self,row):
        """获取第一行的caseID"""
        return self.getValue(row=row,col=ExcelValues().getCaseID)

    def getUrl(self,row):
        """获取请求地址"""
        url =  self.getValue(row=row, col=ExcelValues().getUrl)
        if '{bookID}' in url:
            return str(url).replace('{bookID}',readContent())
        else:
            return url

    def getData(self,row):
        """获取请求参数"""
        return self.getValue(row=row,col=ExcelValues().getData)

    def getMethod(self,row):
        """获取请求方法"""
        return self.getValue(row=row, col=ExcelValues().getMethod)

    def getJson(self,row):
        """建立映射，通过yaml获取参数"""
        return (self.dictYaml()[self.getData(row=row)])

    def getExpect(self,row):
        """获取参数"""
        return self.getValue(row=row,col=ExcelValues().getExpect)

if __name__ == '__main__':
    obj=OpenreationExcel()
    # print(obj.getUrl(row=4))
    # print(obj.getJson(row=4)
    # obj.getData(3)