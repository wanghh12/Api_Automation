import os

# re =requests.post(url="http://tpshop-test.itheima.net/index.php",
#                   data={"username": "15698017292","pasword": "123456","verify_code" : "8888"},
#                   headers={"Content-Type":"text/html; charset=UTF-8"})
# print(re.status_code)

# with open("./data/logindata.json",mode="r",encoding="utf-8") as f:
#     # print(json.load(f))
#     # print(type(json.load(f)))
#     read_data = []
#     for data in json.load(f):
#         # print(tuple(data.values()))
#         read_data.append(tuple(data.values()))
#     print(read_data)

path = os.path.dirname(__file__)
print(path)