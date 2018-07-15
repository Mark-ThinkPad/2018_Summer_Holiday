from selenium import webdriver
import time as tm
import requests
import re
import lxml
from bs4 import BeautifulSoup
from pymongo import MongoClient
from selenium.webdriver.chrome.options import Options

# 登陆
def func(user_id, password):
    Url = "http://221.233.24.23/eams/login.action"
    InfoUrl = "http://221.233.24.23/eams/stdDetail.action"
    GradeUrl = "http://221.233.24.23/eams/teach/grade/course/person!historyCourseGrade.action?projectType=MAJOR"
    driver = webdriver.Chrome()
    driver.get(Url)
    username = driver.find_element_by_id("username")
    passwd = driver.find_element_by_id("password")
    submit = driver.find_element_by_name("submitBtn")
    username.send_keys(user_id)
    passwd.send_keys(password)
    submit.click()
    #print(driver.page_source)

    # 准备数据库
    #client = MongoClient("localhost", 27017)
    #db = client["mydb"]
    #col = db["thc"]

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
        #print(tds)
        if len(tds) < 2:
            continue
        #print("-------------------------------")
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
    #print(time)
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
    #print("-----"*20)
    #print(point_trs)
    for point_tr in point_trs[1:-2]:
        point = {}
        point_tds = point_tr.find_all("td")
        for idx, point_td in enumerate(point_tds):
            point[point_keys[idx]] = point_td.getText()
        points.append(point)
    #print(points)
    #print("-----"*20)

    for grades_tr in grade_trs[1:]:
        grade = {}
        grades_tds = grades_tr.find_all("td")
        for idx, grade_td in enumerate(grades_tds):
            grade[grade_keys[idx]] = grade_td.getText().strip()
        grades.append(grade)
    #print(grades)

    # 下面整理数据
    infos["统计时间"] = time
    infos["绩点"] = points
    infos["总绩点"] = all_point
    infos["成绩"] = grades
    infos["user_id"] = user_id
    infos["passwd"] = passwd
    return infos