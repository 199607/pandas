import os
import pandas as pd
from sqlalchemy import create_engine
import pymysql

#根目录
path = r'D:\datamining\数据\浪潮国家局粮情数据\粮情'

id = 0

for file in os.listdir(path):
        #添加完整文件的目录地址
        file_path = os.path.join(path, file)
        #将路径地址写入data
        data = pd.read_excel(file_path)
        #创建数据库连接
        engine = create_engine('mysql+pymysql://root:root@localhost:3306/test', encoding='utf-8')
        #数据导入
        data.to_sql(file, con=engine, if_exists='replace', index='Flase')
        #变量自增
        id=id+1

# read=os.listdir("D:\datamining\数据\浪潮国家局粮情数据\粮情")
# print(read)