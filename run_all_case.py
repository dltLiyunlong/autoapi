import os
import pytest
import allure

if __name__ == '__main__':
    pytest.main(['-s', ''])
    pytest.main(['-s', '-q', '--alluredir', 'F:/autop/reports/result', ])
    split = 'allure ' + 'generate ' + 'F:/autop/reports/result ' + '-o ' + 'F:/autop/reports/html ' + '--clean'
    os.system('cd F:/autop/reports')
    os.system(split)
    print(split)
