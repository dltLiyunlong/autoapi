from common.readFile import ReadData
from common.Requests import RunMethod
import json
import pytest

request = RunMethod()
data = ReadData().get_excel('/testcase.xls', 'test')
yaml_data = ReadData().get_yaml()


class Test_1(object):
    @pytest.mark.parametrize("Function,CaseName,Type,Run,URL,Headers,Param,Expect", data)
    def test_1(self, Function, CaseName, Type, Run, URL, Headers, Param, Expect):

        print( Expect)


if __name__ == '__main__':
    pytest.main(['-s',r'F:\autop\testcase\zz.py'])
