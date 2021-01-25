import pytest

from common.login import Login


@pytest.fixture(scope='session')
def get_token():
    result = Login().efen_login()
    return result['data']['accessToken']
