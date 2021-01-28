import pytest
import allure
from common.readFile import ReadData
from common.Requests import RunMethod
from common.assertion import Assertion
import json


class Test(object):
    request = RunMethod()
    data = ReadData().get_excel('/testcase.xls', 'test')
    yaml_data = ReadData().get_yaml()
    assersion = Assertion()

    @allure.feature('登录功能')
    @allure.story('登录')
    @allure.title('登录测试用例')
    @pytest.mark.parametrize("Function,CaseName,Type,Run,URL,Headers,Param,Expect", data)
    def test_get_userinfo(self, Function, CaseName, Type, Run, URL, Headers, Param, Expect):
        req = self.request.run_main(Type, self.yaml_data['dr_jg_host'] + URL, json.loads(Headers), json.loads(Param))
        self.assersion.get_response_data(req, Expect)
        self.assersion.asser(Function, CaseName, Expect, req)


if __name__ == '__main__':
    pytest.main(["-s", "-q", '--alluredir', 'F:/autop/reports/result', 'test_userinfo.py'])
