# 2018.7.13 传统爬虫的的实现

---

## Content

<!-- TOC -->

- [2018.7.13 传统爬虫的的实现](#2018713-传统爬虫的的实现)
    - [Content](#content)
    - [传统爬虫的实现](#传统爬虫的实现)
    - [Python3日常复习](#python3日常复习)

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

(1) get方法实现模拟登录
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

(2) 用post方法实现模拟登陆

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

## Python3日常复习

- 等待用户输入
```python
#!/usr/bin/python3
# 以下代码中 ，"\n\n"在结果输出前会输出两个新的空行。一旦用户按下 enter 键时，程序将退出。
input("\n\n按下 enter 键后退出。")
```

- 在同一行显示多行语句使用`;`分号分隔(类似于C语言)

- 多个语句构成代码组(块): 像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组.
```python
if expression : 
   suite
elif expression : 
   suite 
else : 
   suite
```
- print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end="".
```python
print( x, end=" " )
```

- 多个变量赋值
```python
a = b = c = 1
a, b, c = 1, 2, "runoob"
```

- 标准数据类型