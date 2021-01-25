from common.readFile import ReadData
from common.Requests import RunMethod

request = RunMethod.run_main
data = ReadData().get_excel('/testcase.xls', 'test')
yaml_data = ReadData().get_yaml()

req = request(str(data[0][2]),url=yaml_data['dr_jg_host'] + data[0][4], data=data[0][6],
              headers=data[0][5])

print(req)
