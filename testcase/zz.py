from common.readFile import ReadData
from common.Requests import RunMethod
import json

request = RunMethod()
data = ReadData().get_excel('/testcase.xls', 'test')
yaml_data = ReadData().get_yaml()

req = request.run_main(data[0][2], yaml_data['dr_jg_host']+data[0][4], json.loads(data[0][6]), json.loads(data[0][5]))

print(req)
