import pytest
import allure
from common.readFile import ReadData
from common.Requests import RunMethod
import json


class Test(object):
    request = RunMethod()
    data = ReadData().get_excel('/testcase.xls', 'test')
    yaml_data = ReadData().get_yaml()

    @allure.feature('获取用户信息功能')
    @allure.story('获取用户信息')
    @allure.title('获取用户信息')
    def test_get_userinfo(self):
        req = self.request.run_main(self.data[0][2], self.yaml_data['dr_jg_host'] + self.data[0][4],
                                    json.loads(self.data[0][6]),
                                    json.loads(self.data[0][5]))

        assert req['success'] == True


if __name__ == '__main__':
    pytest.main(["-s", "-q", '--alluredir', 'F:/autop/reports/result', 'test_userinfo.py'])
