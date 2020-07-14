from base.method import Requsts
from common.public import *
from utils.operationExcel2 import *
import pytest
import json
excel=OpenreationExcel()
obj=Requsts()

@pytest.mark.parametrize('datas',excel.run())
def test_login_book(datas):

    params=datas[ExcelValue.params]
    if len(str(params).strip())==0:pass
    elif len(str(params).strip())>0:
        params = json.loads(params)

    header = datas[ExcelValue.headers]
    if len(str(header).strip()) == 0:
        pass
    elif len(str(header).strip()) > 0:
        header = json.loads(header)

    r=obj.post(url=excel.case_prev(datas[ExcelValue.casePre])[ExcelValue.caseUrl],
    json=json.loads(excel.case_prev(datas[ExcelValue.casePre])[ExcelValue.params])
    )

    prevResult=r.json()["access_token"]
    header=excel.prvHeaders(prevResult)

    status_code=int(datas[ExcelValue.statusCode])

    def case_assert_resule(r):
        assert r.status_code == status_code
        assert datas[ExcelValue.expect] in json.dumps(r.json(),ensure_ascii=False)

    def getUrl():
        return str(datas[ExcelValue.caseUrl]).replace('{bookID}', readContent())

    if datas[ExcelValue.method]=='get':
        if '/books' in datas[ExcelValue.caseUrl]:
            r=obj.get(url=datas[ExcelValue.caseUrl],headers=header)
        else:
            r=obj.get(url=getUrl(),headers=header)
        case_assert_resule(r=r)
    elif  datas[ExcelValue.method]=='post':
        r = obj.post(url=datas[ExcelValue.caseUrl],
                     json=excel.params(),
                     headers=header)
        case_assert_resule(r=r)

    elif  datas[ExcelValue.method]=='put':
        r=obj.put(url=getUrl(),
                  json=excel.params(),
                  headers=header)
        case_assert_resule(r=r)
    elif datas[ExcelValue.method]=='delete':
        r = obj.delete(url=getUrl(),
                       headers=header)
        case_assert_resule(r=r)



if __name__ == '__main__':
    pytest.main(["-s","-v","test_login_book.py"])