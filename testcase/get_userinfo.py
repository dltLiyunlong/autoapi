import pytest
import allure
from common.readFile import ReadData
from common.Requests import RunMethod


class Test(object):
    request = RunMethod.run_main
    data = ReadData().get_excel('/testcase.xls', 'test')
    yaml_data = ReadData().get_yaml()

    @allure.feature('获取用户信息功能')
    @allure.story('获取用户信息')
    @allure.title('获取用户信息-标题')
    def test_get_userinfo(self):
        req = self.request(self.data[0][2], self.yaml_data['dr_jg_host'] + self.data[0][4], data=self.data[0][6],
                           headers=self.data[0][5])
        print(req)

if __name__ == '__main__':
    pytest.main(["-s", "-q", '--alluredir', 'F:/apiauto/reports/result', 'get_userinfo.py'])
