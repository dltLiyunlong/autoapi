import requests
import urllib3
from urllib3 import encode_multipart_formdata
from common.logs import Log


class RunMethod(object):
    log = Log()
    urllib3.disable_warnings()

    def post_main(self, url, headers, data):
        res = requests.post(url=url, headers=headers, json=data)
        return res.json()

    def get_main(self, url, headers):
        res = requests.post(url=url, headers=headers)
        return res.json()

    def run_main(self, method, url, headers, data):
        try:
            if method == 'post':
                res = self.post_main(url, headers, data)
            elif method == 'get':
                res = self.get_main(url, headers)
            else:
                return '参数错误'
            return res

        except Exception as e:
            self.log.error('检查参数：{}'.format(e))


if __name__ == '__main__':
    print('')
