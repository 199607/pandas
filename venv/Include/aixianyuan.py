import requests
from  lxml import etree
from selenium import webdriver




# chrome = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
# chrome.get('https://www.bilibili.com')
# ul = chrome.find_element_by_xpath('//nav[@id = "main-nav"]/ul')
# lis = ul.find_elements_by_xpath('li')
# print(len(lis))


url='http://www.aixianyuan.cn'   #输入我们的url
get = requests.get(url).text   # get(url) 得到我们的网页, text将源网页转化为字符串
selector = etree.HTML(get) # 将源码转换为xpath可以识别的TML格式

info = {}  #字典用于储存信息
names = driver.find_element_by_xpath('//nav[@id = "main-nav"]//ul/li')
for i in range(names):

    info['xinxi'] = selector.xpath('//nav[@id = "main-nav"]//ul/li/text()') # 定位
    #names = driver.find_element_by_xpath('//nav[@id = "main-nav"]//ul/li')
    #print(info)

print(info)