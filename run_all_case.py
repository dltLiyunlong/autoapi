import os
import pytest
import allure

if __name__ == '__main__':
    pytest.main(["-sq",
                 "--alluredir", "./allure-results"])
    os.system(r"allure generate --clean allure-results -o allure-report")
