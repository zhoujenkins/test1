# @Time    : 2020/5/30 14:31
# @Author  : Jennings
# @Email   : zjn@wiwi.ink

import pytest
import allure
# 88a291f935e3408ab14ae0467a79865f


class Test_alluer_001:

    def setup(self):
        print("start................")

    def teardown(self):
        print("end................")

    @allure.step(title="第一个测试")
    def test_001(self):
        assert 0

    def test_002(self):
        assert 1


if __name__ == '__main__':
    pytest.main(['-s','test_allure001.py'])