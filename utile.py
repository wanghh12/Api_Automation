# 读取测试数据
import json
import os
def readdata(file):
    try:
        path = os.path.dirname(__file__)+"\data\\"+file
        read_data=[]
        with open(path, mode="r", encoding="utf-8") as f:
            for data in json.load(f):
                read_data.append(tuple(data.values()))
            return read_data
    except FileNotFoundError:
        print(f"--------------读取的  {file}  数据文件没有找到----------------")
        print(f"加载的path路径为:{path}")
