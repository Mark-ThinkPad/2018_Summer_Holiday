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

    

