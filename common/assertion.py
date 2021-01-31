from common.logs import Log


class Assertion():
    log = Log()
    response_values = []

    def get_response_data(self, response_data, keys=[]):
        '''
        获取接口响应数据组合list
        :param response_data:
        :param keys:
        :return:
        '''
        try:
            if isinstance(response_data, list):
                for value in response_data:
                    if isinstance(value, list) or isinstance(value, dict):
                        self.get_response_data(value, keys)
            elif isinstance(response_data, dict):
                for i, j in sorted(response_data.items()):
                    if i in keys:
                        self.response_values.append(j)
                    else:
                        self.get_response_data(j, keys)
            else:
                pass
        except Exception as e:
            self.log.error("获取接口响应数据组合list报错{}".format(e))

    def asser(self, function, casename, expect, response_data):

        try:
            assert expect == response_data['message']
            assert expect == response_data['message']
            self.log.info('{}--{}【pass】'.format(function, casename))

        except Exception as e:
            self.log.error('{}--{}【pass】{}'.format(function, casename, e))


if __name__ == '__main__':
    print('断言方法')
    print('zz')

