import requests


class TestMianApi(object):
    def __init__(self):
        # 创建session实例
        self.session=requests.Session()
        self.tpshop_url="http://hmshop-test.itheima.net"
        # self.tpshop_url1="http://127.0.0.1/"
        self.headers = {"Content-Type":"application/x-www-form-urlencoded"}

    def log01(self,data):# 获取验证码
        self.url_verify=self.session.get(url=self.tpshop_url+"/index.php?m=Home&c=User&a=verify&r=0.7823192290498644")
        return self.session.post(url=self.tpshop_url+"/index.php?m=Home&c=User&a=do_login&t=0.5490331210500934",headers=self.headers,data=data)
        # return requests.post(url=self.tpshop_url+"/index.php?m=Home&c=User&a=do_login&t=0.5490331210500934",headers=self.headers,data=data)


if __name__ == '__main__':
    testmianapi = TestMianApi()
    res = testmianapi.log01(data={"username": "15698017292", "pasword": "123458", "verify_code": "8888"})
    print(res.json())
