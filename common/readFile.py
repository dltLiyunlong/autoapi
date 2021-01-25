import yaml
import xlrd
import os
import sys


class ReadData(object):

    def __init__(self):
        self.path = os.path.abspath(
            os.path.dirname(os.path.dirname(__file__)) + '/config/test/data.yaml')
        self.file = os.path.abspath(
            os.path.dirname(os.path.dirname(__file__)) + '/config')

    # 读取yaml配置文件
    def get_yaml(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            return yaml.load(f, Loader=yaml.FullLoader)

    # 读取测试用例
    def get_excel(self, file_name, sheet_name):
        book = xlrd.open_workbook(self.file + file_name)
        sheet = book.sheet_by_name(sheet_name)
        param = []
        for i in range(1, sheet.nrows):
            param.append(sheet.row_values(i))
        return param


if __name__ == '__main__':
    data = ReadData()
