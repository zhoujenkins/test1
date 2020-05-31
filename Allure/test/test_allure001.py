# @Time    : 2020/5/30 14:31
# @Author  : Jennings
# @Email   : zjn@wiwi.ink

import pytest


class Test_alluer_001:

    def setup(self):
        print("start................")
        pass

    def teardown(self):
        print("end................")
        pass

    def test_001(self):
        assert True


if __name__ == '__main__':
    pytest.main(['-s','test_allure001.py'])