import pandas as pd
from pandas import DataFrame, Series
from sqlalchemy import create_engine
import time

#开始时间
start = time.time()
#创建数据库链接
engine = create_engine('mysql+pymysql://root:root@localhost:3306/test', encoding='utf-8')
#查询语句
sql = '''select * from guangdon;'''
#读取mysql
df = pd.read_sql_query(sql,engine)
print("从MySQL成功读取数据，开始将数据导入excel表格中。。。")
#将读取的数据转换成dataframe类型
test_data = DataFrame.from_records(df)
#将数据写入excel中
test_data.to_excel("D:\\datatest\\sqldata.xlsx",index=False)

print("导入成功")
#打印时间
end = time.time()