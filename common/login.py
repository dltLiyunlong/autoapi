from common import Requests
from common.readFile import ReadData
from common.logs import Log
import json

yaml_data = ReadData().get_yaml()
headers = {"Content-Type": "application/json"}
data = {"userName": yaml_data['dr_org_user']['username'],
        "password": yaml_data['dr_org_user']['password']}


class Login(object):
    log = Log()
    request = Requests.RunMethod()

    def efen_login(self):
        res = self.request.run_main('post', yaml_data['dr_jg_host'] + 'api/user/login', data, headers)
        return res



