from common.readFile import ReadData
from common.Requests import RunMethod

request = RunMethod.run_main
data = ReadData().get_excel('/testcase.xls', 'test')
yaml_data = ReadData().get_yaml()



print(data)
print('data')


