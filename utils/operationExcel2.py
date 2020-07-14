import xlrd
from common.public import *
import json

class ExcelValue:
    caseID = "测试用例ID"
    caseModel = "模块"
    caseName = "接口名称"
    caseUrl = "请求地址"
    casePre = "前置条件"
    method = "请求方法"
    paramsType = "请求参数类型"
    params = "请求参数"
    expect = "期望结果"
    isRun = "是否运行"
    headers = "请求头"
    statusCode = "状态码"

class OpenreationExcel():
    def getSheet(self):
        book=xlrd.open_workbook(filePath(fileDir='data',fileName='api.xlsx'))
        return book.sheet_by_index(0)

    @property
    def getExcelDatas(self):
        """获取表格中所有内容"""
        datas=[]
        title=self.getSheet().row_values(0)
        # 按行循环获取表格中的内容，从1开始表示忽略首行
        for row in range(1,self.getSheet().nrows):
            row_values=self.getSheet().row_values(row)
            # zip 把两个值搞成字典
            datas.append(dict(zip(title,row_values)))
        return datas

    def run(self):
        """获取可执行用例"""
        run_list=[]
        for item in self.getExcelDatas:
            isRun=item[ExcelValue.isRun]
            if isRun == 'y':run_list.append(item)
            else:pass
        return run_list

    def case_lists(self):
        """获取excel中所有测试点"""
        cases=[]
        for item in self.getExcelDatas:
            cases.append(item)
        return cases


    def params(self):
        """对请求参数为空做处理"""
        params_list=[]
        for item in self.run():
            params=item[ExcelValue.params]
            if len(str(params).strip())==0:pass
            elif len(str(params).strip())>0:
                params=json.loads(params)
                return params

    def case_prev(self,casePrev):
        """依据前置条件找关联的测试用例"""
        for item in self.case_lists():
            if casePrev in item.values():
                return item
        return None

    def prvHeaders(self,prevResult):
        """替换请求头中的token"""
        for item in self.run():
            headers = item[ExcelValue.headers]
            if '{token}' in headers:
                headers=str(headers).replace('{token}',prevResult)
                return json.loads(headers)




if __name__ == '__main__':
    obj=OpenreationExcel()
    obj.prvHeaders('4243')