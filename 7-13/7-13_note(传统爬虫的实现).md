# 2018.7.13 传统爬虫的的实现

---

## Content

<!-- TOC -->

- [2018.7.13 传统爬虫的的实现](#2018713-传统爬虫的的实现)
    - [Content](#content)
    - [传统爬虫的实现](#传统爬虫的实现)
        - [(1) get方法实现模拟登录](#1-get方法实现模拟登录)
        - [(2)排版美化版](#2排版美化版)
        - [(3) 用post方法实现模拟登陆](#3-用post方法实现模拟登陆)
        - [(4)将爬到的数据写入数据库](#4将爬到的数据写入数据库)
        - [当天的作业, 爬取教务处的成绩](#当天的作业-爬取教务处的成绩)
    - [Python3日常复习](#python3日常复习)
        - [等待用户输入](#等待用户输入)
        - [在同一行显示多行语句使用`;`分号分隔(类似于C语言)](#在同一行显示多行语句使用分号分隔类似于c语言)
        - [多个语句构成代码组(块): 像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组.](#多个语句构成代码组块-像ifwhiledef和class这样的复合语句首行以关键字开始以冒号--结束该行之后的一行或多行代码构成代码组)
        - [print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end="".](#print-默认输出是换行的如果要实现不换行需要在变量末尾加上-end)
        - [多个变量赋值](#多个变量赋值)
        - [标准数据类型](#标准数据类型)

<!-- /TOC -->

---

## 传统爬虫的实现

1. 复制cookies(F12菜单进入Network选项找到login.action)(在home.action中找cookie也是可用的)

Request cookies
```
semester.id=48; JSESSIONID=BA91DE009F3EE413101F0AAF1F801E86.node137; adc-ck-jwxt_pools=IJALAKAK; GSESSIONID=BA91DE009F3EE413101F0AAF1F801E86.node137
```

Response cookies
```
adc-ck-jwxt_pools=IJALAKAK; Expires=Fri, 13-Jul-2018 01:44:15 GMT; Path=/
```

2. 复制User-Agent

```
Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0
```

### (1) get方法实现模拟登录
```python
from bs4 import BeautifulSoup
import requests
import time as tm

Header = {
        "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0",
        "Cookie":"JSESSIONID=EFD47CFA92DC3A0418F90076DD01FFDB.node137; adc-ck-jwxt_pools=IJALAKAK; GSESSIONID=EFD47CFA92DC3A0418F90076DD01FFDB.node137"
        }

Url = "http://jwc3.yangtzeu.edu.cn/eams/stdDetail.action"

req = requests.get(Url, headers=Header)
print(req.text)

```
---

### (2)排版美化版
```python
from bs4 import BeautifulSoup
import requests
import time as tm
import hashlib
import re
import lxml

def get_str_sha(str):
    sha = hashlib.sha1(str)
    return sha.hexdigest()
user_id = "201703407"
passwd = "201703407"

Header = {
        "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0",
        #"Cookie":"JSESSIONID=EFD47CFA92DC3A0418F90076DD01FFDB.node137; adc-ck-jwxt_pools=IJALAKAK; GSESSIONID=EFD47CFA92DC3A0418F90076DD01FFDB.node137"
        }

Url = "http://jwc3.yangtzeu.edu.cn/eams/stdDetail.action"
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
print(req.text)

InfoUrl = "http://jwc3.yangtzeu.edu.cn/eams/stdDetail.action"
req = s.get(InfoUrl)
html = req.text
soup = BeautifulSoup(html, "lxml")
trs = soup.find_all("tr")
for tr in trs[1:-1]:
    tds = tr.find_all("td")
    if len(tds) < 2:
        continue
    print("-------------------------------")
    key1 = tds[0].getText()
    val1 = tds[1].getText()
    key2 = tds[2].getText()
    val2 = tds[3].getText()
    print(key1+val1+"\t"+key2+val2)
    '''
    for idx, td in enumerate(tds):
        if idx in [4]:
            continue
        print(td.getText())
    '''
```

---

### (3) 用post方法实现模拟登陆

```python
from bs4 import BeautifulSoup
import requests
import time as tm
import hashlib
import re

def get_str_sha(str):
    sha = hashlib.sha1(str)
    return sha.hexdigest()
user_id = "201703407"
passwd = "201703407"

Header = {
        "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0",
        #"Cookie":"JSESSIONID=EFD47CFA92DC3A0418F90076DD01FFDB.node137; adc-ck-jwxt_pools=IJALAKAK; GSESSIONID=EFD47CFA92DC3A0418F90076DD01FFDB.node137"
        }

Url = "http://jwc3.yangtzeu.edu.cn/eams/stdDetail.action"
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
print(req.text)
```

---

### (4)将爬到的数据写入数据库
```python
from bs4 import BeautifulSoup
import requests
import time as tm
import hashlib
import re
import lxml
from pymongo import MongoClient

def get_str_sha(str):
    sha = hashlib.sha1(str)
    return sha.hexdigest()
user_id = "201703407"
passwd = "201703407"

Url = "http://jwc3.yangtzeu.edu.cn/eams/stdDetail.action"
LoginUrl = "http://jwc3.yangtzeu.edu.cn/eams/login.action"
client = MongoClient("localhost", 27017)
db = client["mydb"]
col = db["students"]
Header = {
        "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0",
        #"Cookie":"JSESSIONID=EFD47CFA92DC3A0418F90076DD01FFDB.node137; adc-ck-jwxt_pools=IJALAKAK; GSESSIONID=EFD47CFA92DC3A0418F9    0076DD01FFDB.node137"
          }

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
print(req.text)

InfoUrl = "http://jwc3.yangtzeu.edu.cn/eams/stdDetail.action"
req = s.get(InfoUrl)
html = req.text
soup = BeautifulSoup(html, "lxml")
trs = soup.find_all("tr")
infos = {}
keys = []
vals = []
for tr in trs[1:-1]:
    tds = tr.find_all("td")
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
#print(key1+val1+"\t"+key2+val2)
'''
for idx, td in enumerate(tds):
    if idx in [4]:
        continue
    print(td.getText())
'''

col.insert_one(infos)    


```

### 当天的作业, 爬取教务处的成绩

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
n = 0
for tr in trs[3:]:
    tds = tr.find_all("td")
    if len(tds) < 1:
        continue
    print("---------------------")
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
    print(infos)
    #col.insert(infos, '_id'='5b48ae4eac3b721dd959e9f' + str(n))
    #n = n + 1
```
---

## Python3日常复习

### 等待用户输入
```python
#!/usr/bin/python3
# 以下代码中 ，"\n\n"在结果输出前会输出两个新的空行。一旦用户按下 enter 键时，程序将退出。
input("\n\n按下 enter 键后退出。")
```

### 在同一行显示多行语句使用`;`分号分隔(类似于C语言)

### 多个语句构成代码组(块): 像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组.
```python
if expression : 
   suite
elif expression : 
   suite 
else : 
   suite
```
### print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end="".
```python
print( x, end=" " )
```

### 多个变量赋值
```python
a = b = c = 1
a, b, c = 1, 2, "runoob"
```

### 标准数据类型

- (1)Number(数字)
- (2)String(字符串)
- (3)List(列表)
- (4)Tuple(元组)
- (5)Set(集合)
- (6)Dictionary(字典)

> Python3 的六个标准数据类型中：
- 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组)
- 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）