import pytest
import requests

import utile
from api.projectapi import TestMianApi


class TestMianClass:
    def setup_class(cls):
        cls.testmian = TestMianApi()

    def setup(self):
        pass
    # def teardown(self):
    #     pass


    ##测试登录接口
    @pytest.mark.parametrize(("username","password","verify_code","excepts"),utile.readdata("logindata.json"))##参数化
    def test_login(self,username,password,verify_code,excepts):
        data = {"username":username,"password":password,"verify_code":verify_code}
        # print(data)
        res =self.testmian.log01(data=data)
        assert  res.json().get("msg") == excepts
        # print(res.json())

    def test_jiagou(self):
        pass



