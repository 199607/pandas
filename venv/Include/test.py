from sqlalchemy import create_engine
import pymysql
import pandas as pd

io = r'D:\\广东.csv'

data = pd.read_csv(io,encoding="utf-8")
print(data)
print("----------------------------------------------")
#df=pd.DataFrame(data)


#df = pd.DataFrame(pd.read_excel(io))

#引用多行作为列 header
#data = pd.read_excel(io, sheet_name = 'csgo', header = [0,1])

#对列名重新赋值 names长度一定要和excel一致！！！
#data = pd.read_excel(io, sheet_name = 'csgo',names = ['rank','player','club','goal','common_goal','penalty'])

#可以是工作表列名称，如index_col = '排名'；可以是整型或整型列表，如index_col = 0 或 [0, 1]，如果选择多个列，则返回多重索引。
#data = pd.read_excel(io, sheet_name = 'csgo', index_col = '企业代码')

# 选取特定数据  0可以使用整型，从0开始，如[0,2,3]；
#可以使用Excel传统的列名“A”、“B”等字母，如“A：C, E” ="A, B, C, E"，注意两边都包括。
#usecols 可避免读取全量数据，而是以分析需求为导向选择特定数据，可以大幅提高效率。#
#data = pd.read_excel(io, sheet_name = 'csgo', usecols = [0, 1, 3])

#强制类型转换  converters = {'排名': str, '场次': int}，
#将“排名”列数据类型强制规定为字符串（pandas默认将文本类的数据读取为整型），“场次”列强制规定为整型
#data = pd.read_excel(io, sheet_name = 'csgo', converters = {'排名': str, '场次': float})

#跳过特定行 skiprows= n， 跳过前n行； skiprows = [a, b, c]，跳过第a+1,b+1,c+1行（索引从0开始）；
#使用skiprows 后，有可能首行（即列名）也会被跳过。
#data = pd.read_excel(io, sheet_name = 'csgo', skiprows = [1,2,3])

#如果只想了解Excel的列名及概况，不必读取全量数据，nrows会十分有用。
#data = pd.read_excel(io, sheet_name = 'csgo', nrows = 3)

#跳过末尾 n行
#data = pd.read_excel(r'C:\Users\Administrator\Desktop\data.xlsx' , sheet_name = 'csgo', skipfooter = 43)



#print(df.head())
#print(data.head())
#df.info()

# # ---------------------------数据库第一种链接--------------------------
# # 打开数据库连接

# db = pymysql.connect("localhost", "root", "root", "datamining", charset='utf8' )
# #
#
# data.to_sql('guangdon',con=db,if_exists='replace',index='Flase')


#-------------------------数据库第二种链接-----------------------

engine =create_engine('mysql+pymysql://root:root@localhost:3306/test',encoding='utf-8')

data.to_sql('guangdon',con=engine,if_exists='replace',index='Flase')

#<------------------------链接测试------------------------------>
'''
# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

print ("Database version : %s " % data)
'''


'''
# 如果数据表已经存在使用 execute() 方法删除表。
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 创建数据表SQL语句--------------------------------------------
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)
'''
#SQL 插入语句---------------------------------------------
'''# SQL 插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()'''
# 关闭数据库连接
#db.close()