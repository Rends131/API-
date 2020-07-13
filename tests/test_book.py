from base.method import Requsts
from utils.operationExcel import OpenreationExcel
from utils.operationYaml import OperationYaml
from common.public import *
import pytest
import json

class TestBook:
    excel=OpenreationExcel()
    obj=Requsts()

    def ruselt(self,r,row):
        assert r.status_code ==200
        assert self.excel.getExpect(row=row) in json.dumps(r.json(),ensure_ascii=False)

    def test_book_001(self):
        """获取所有书籍信息"""
        r=self.obj.get(url=self.excel.getUrl(row=1))
        self.ruselt(r=r,row=1)

    def test_book_002(self):
        """添加书籍信息"""
        r=self.obj.post(url=self.excel.getUrl(row=2),
                        json=self.excel.getJson(row=2))
        writecContet(content=r.json()[0]['datas']['id'])
        self.ruselt(r=r,row=2)


    def test_book_003(self):
        """获取所有书籍信息"""
        r=self.obj.get(url=self.excel.getUrl(row=3))
        self.ruselt(r=r,row=3)

    def test_book_004(self):
        """修改书籍"""
        r=self.obj.put(url=self.excel.getUrl(row=4),
                       json=self.excel.getJson(row=4))
        self.ruselt(r=r,row=4)


    def test_book_005(self):
        """删除书籍"""
        r=self.obj.delete(url=self.excel.getUrl(row=5))
        self.ruselt(r=r,row=5)



if __name__ == '__main__':
    pytest.main(["-s", "-v", "test_book.py::TestBook"])