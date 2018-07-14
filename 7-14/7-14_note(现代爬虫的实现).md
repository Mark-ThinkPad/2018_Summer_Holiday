# 2018.7.14 现代爬虫的实现

---

## Content

<!-- TOC -->

- [2018.7.14 现代爬虫的实现](#2018714-现代爬虫的实现)
    - [Content](#content)
    - [昨天晚上的作业(爬成绩)((文件为SpiderHW.py))](#昨天晚上的作业爬成绩文件为spiderhwpy)
    - [现代爬虫的实现](#现代爬虫的实现)
        - [第一版能用的程序(实现了模拟登陆和点击)](#第一版能用的程序实现了模拟登陆和点击)
        - [终极完成版](#终极完成版)
    - [Ajax](#ajax)

<!-- /TOC -->

---

## 昨天晚上的作业(爬成绩)((文件为SpiderHW.py))

1. 首先分析网页的结构

2. 从tables入手, 学期总绩点为第一个table, 各门课的成绩为第二个table

```python
from bs4 import BeautifulSoup # 解析网页
import requests # 主要使用get和post方法, get方法获取网页, post方法提交请求
import time as tm # 避免出现"请勿点击过快的"情况
import hashlib # 密码是经过加密的, 获取加密后的密码需要借助哈希加密的库
import re # 正则表达式
import lxml #C写的库, 速度比bs快, 同样是解析网页的作用
from pymongo import MongoClient # 使用Python语言对mongodb数据库进行操作

# 使用post方法实现虚拟登录
def get_str_sha(str):
    sha = hashlib.sha1(str)
    return sha.hexdigest()
user_id = "201703407"
passwd = "201703407"

Header = {
        "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0",
        #"Cookie":"JSESSIONID=EFD47CFA92DC3A0418F90076DD01FFDB.node137; adc-ck-jwxt_pools=IJALAKAK; GSESSIONID=EFD47CFA92DC3A0418F90076DD01FFDB.node137"
        }

LoginUrl = "http://jwc3.yangtzeu.edu.cn/eams/login.action"
s = requests.Session()

req = s.get(LoginUrl)
html = req.text

res = re.search("CryptoJS.SHA1\(\'(.*)\' ", html)
opasswd = res.group(1)
passwd = get_str_sha((opasswd+passwd).encode("utf-8"))
print(passwd)

tm.sleep(1);

Data = {
        "username":user_id,
        "password":passwd,
        "encodedPassword:":"",
        "session_locale":"zh_CN",
        }

req = s.post(LoginUrl, data=Data)
#print(req.text)

# 获取成绩页面

GradeUrl = "http://jwc3.yangtzeu.edu.cn/eams/teach/grade/course/person!historyCourseGrade.action?projectType=MAJOR"
req = s.get(GradeUrl) # 获取成绩页面
html = req.text # 返回一个文本
#print(html)
soup = BeautifulSoup(html, "lxml") # 创建一个对象
trs = soup.find_all("tr") # 找到所有tr标签
infos = {}
keys = []
vals = []

# s上数据库
client = MongoClient("localhost", 27017)
db = client["scoredb"]
col = db["score"]
'''
n = 0
for tr in trs[3:]:
    tds = tr.find_all("td")
    if len(tds) < 1:
        continue
    #print("---------------------")
    key1 = "学年学期"
    key2 = "课程代码"
    key3 = "课程序号"
    key4 = "课程名称"
    key5 = "课程类别"
    key6 = "学分"
    key7 = "总评成绩"
    key8 = "最终"
    key9 = "绩点"
    keys.append(key1)
    keys.append(key2)
    keys.append(key3)
    keys.append(key4)
    keys.append(key5)
    keys.append(key6)
    keys.append(key7)
    keys.append(key8)
    keys.append(key9)
    val1 = tds[0].getText().strip()
    val2 = tds[1].getText().strip()
    val3 = tds[2].getText().strip()
    val4 = tds[3].getText().strip()
    val5 = tds[4].getText().strip()
    val6 = tds[5].getText().strip()
    val7 = tds[6].getText().strip()
    val8 = tds[7].getText().strip()
    val9 = tds[8].getText().strip()
    vals.append(val1)
    vals.append(val2)
    vals.append(val3)
    vals.append(val4)
    vals.append(val5)
    vals.append(val6)
    vals.append(val7)
    vals.append(val8)
    vals.append(val9)
    for i in range(len(vals)-1):
        infos[keys[i]] = vals[i]
    #newObjectId = ObjectId()
    #strin=str(n)
    #infos['_id'] = '5b48ae4eac3b721dd959e9f' + strin
    #print(infos)
    #col.insert(infos, '_id'='5b48ae4eac3b721dd959e9f' + str(n))
    #n = n + 1
'''
tables = soup.find_all("table") # 获取观察网页结构筛选table
#print(tables)
#print(len(tables)) # 获取table的个数(len()其实是返回长度的)
point_trs = tables[0].find_all("tr") # 绩点的tr标签们
grade_trs = tables[1].find_all("tr") # 成绩的tr标签们
point_keys = []
all_point_keys = ["类型", "必修门数", "必修总学分", "必修平均绩点"]
grade_keys = []
points = []
grades = []
all_point = {}
point = {}
grade = {}

#print(point_trs)
time = "2"+point_trs[-1].getText().split("2")[-1]# 获取查询时间
print(time)
all_point_ths = point_trs[-2].find_all("th")

for idx, all_point_th in enumerate(all_point_ths): # enumerate()函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
    all_point[all_point_keys[idx]] = all_point_th.getText()
print(all_point)

for point_th in point_trs[0].find_all("th"):
    point_keys.append(point_th.getText())
for grade_th in grade_trs[0].find_all("th"):
    grade_keys.append(grade_th.getText())
print(point_keys)
print(grade_keys)
print("-----"*20)
print(point_trs)
for point_tr in point_trs[1:-2]:
    point = {}
    point_tds = point_tr.find_all("td")
    for idx, point_td in enumerate(point_tds):
        point[point_keys[idx]] = point_td.getText()
    points.append(point)
print(points)
print("-----"*20)

for grades_tr in grade_trs[1:]:
    grade = {}
    grades_tds = grades_tr.find_all("td")
    for idx, grade_td in enumerate(grades_tds):
        grade[grade_keys[idx]] = grade_td.getText().strip()
    grades.append(grade)
print(grades)

# 下面整理数据
infos["统计时间"] = time
infos["绩点"] = points
infos["总绩点"] = all_point
infos["成绩"] = grades

# 下面是插入到数据库
col.insert(infos)
```
---

## 现代爬虫的实现

- 使用`selenium库`和`phantomjs`实现模拟登录, 不需要手动引入`hashlib`

### 第一版能用的程序(实现了模拟登陆和点击)
```python
from selenium import webdriver
import time as tm
from bs4 import BeautifulSoup
from pymongo import MongoClient
from selenium.webdriver.chrome.options import Options

Url = "http://221.233.24.23/eams/login.action"
InfoUrl = "http://221.233.24.23/eams/stdDetail.action"
GradeUrl = "http://221.233.24.23/eams/teach/grade/course/person!historyCourseGrade.action?projectType=MAJOR"
user_id = "201703407"
driver = webdriver.Chrome()
driver.get(Url)
username = driver.find_element_by_id("username")
passwd = driver.find_element_by_id("password")
submit = driver.find_element_by_name("submitBtn")
username.send_keys(user_id)
passwd.send_keys(user_id)
submit.click()
print(driver.page_source)
```

---

### 终极完成版

```python
from selenium import webdriver
import time as tm
import requests
import re
import lxml
from bs4 import BeautifulSoup
from pymongo import MongoClient
from selenium.webdriver.chrome.options import Options

# 登陆
Url = "http://221.233.24.23/eams/login.action"
InfoUrl = "http://221.233.24.23/eams/stdDetail.action"
GradeUrl = "http://221.233.24.23/eams/teach/grade/course/person!historyCourseGrade.action?projectType=MAJOR"
user_id = "201603445"
driver = webdriver.Chrome()
driver.get(Url)
username = driver.find_element_by_id("username")
passwd = driver.find_element_by_id("password")
submit = driver.find_element_by_name("submitBtn")
username.send_keys(user_id)
passwd.send_keys(user_id)
submit.click()
#print(driver.page_source)

# 准备数据库
client = MongoClient("localhost", 27017)
db = client["mydb"]
col = db["thc"]

# 抓学生信息
driver.get(InfoUrl)
html = driver.page_source
soup = BeautifulSoup(html, "lxml")
trs = soup.find_all("tr")
infos = {}
keys = []
vals = []
for tr in trs[1:-1]:
    tds = tr.find_all("td")
    print(tds)
    if len(tds) < 2:
        continue
    print("-------------------------------")
    key1 = tds[0].getText()[:-1]
    val1 = tds[1].getText()
    key2 = tds[2].getText()[:-1]
    val2 = tds[3].getText()
    keys.append(key1)
    keys.append(key2)
    vals.append(val1)
    vals.append(val2)
for i in range(len(vals)-1):
    infos[keys[i]] = vals[i]
print(infos)
col.insert_one(infos)    

# 抓学生成绩
driver.get(GradeUrl) # 获取成绩页面
html = driver.page_source
soup = BeautifulSoup(html, "lxml") # 创建一个对象
trs = soup.find_all("tr") # 找到所有tr标签
tables = soup.find_all("table") # 获取观察网页结构筛选table
#print(tables)
#print(len(tables)) # 获取table的个数(len()其实是返回长度的)
point_trs = tables[0].find_all("tr") # 绩点的tr标签们
grade_trs = tables[1].find_all("tr") # 成绩的tr标签们
point_keys = []
all_point_keys = ["类型", "必修门数", "必修总学分", "必修平均绩点"]
grade_keys = []
points = []
grades = []
all_point = {}
point = {}
grade = {}

#print(point_trs)
time = "2"+point_trs[-1].getText().split("2")[-1]# 获取查询时间
print(time)
all_point_ths = point_trs[-2].find_all("th")

for idx, all_point_th in enumerate(all_point_ths): # enumerate()函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
    all_point[all_point_keys[idx]] = all_point_th.getText()
#print(all_point)

for point_th in point_trs[0].find_all("th"):
    point_keys.append(point_th.getText())
for grade_th in grade_trs[0].find_all("th"):
    grade_keys.append(grade_th.getText())
#print(point_keys)
#print(grade_keys)
print("-----"*20)
#print(point_trs)
for point_tr in point_trs[1:-2]:
    point = {}
    point_tds = point_tr.find_all("td")
    for idx, point_td in enumerate(point_tds):
        point[point_keys[idx]] = point_td.getText()
    points.append(point)
print(points)
print("-----"*20)

for grades_tr in grade_trs[1:]:
    grade = {}
    grades_tds = grades_tr.find_all("td")
    for idx, grade_td in enumerate(grades_tds):
        grade[grade_keys[idx]] = grade_td.getText().strip()
    grades.append(grade)
print(grades)

# 下面整理数据
infoss = {}
infoss["统计时间"] = time
infoss["绩点"] = points
infoss["总绩点"] = all_point
infoss["成绩"] = grades

# 下面是插入到数据库
col.insert(infoss)
```

---

## Ajax

- 异步的js & xml
- 状态码: 200成功
- 必须在同一个域名下使用(同域)
- 基本原理(demo.html)
- 具体实例查看`paging`文件夹