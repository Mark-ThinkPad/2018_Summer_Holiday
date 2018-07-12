# 7.12.note

`Linux environment`

---

## Content

<!-- TOC -->

- [7.12.note](#712note)
    - [Content](#content)
    - [今日培训内容](#今日培训内容)
    - [Debian 9.4.0 安装](#debian-940-安装)
    - [Linux基本命令](#linux基本命令)
    - [Node.js环境搭建](#nodejs环境搭建)
    - [mongodb数据库](#mongodb数据库)
    - [Python双版本的配置](#python双版本的配置)
    - [晚上自习](#晚上自习)
        - [输出Python3关键字](#输出python3关键字)
        - [注释](#注释)
        - [行与缩进](#行与缩进)
        - [多行语句](#多行语句)
        - [数字类型(number)](#数字类型number)
        - [字符串(string)](#字符串string)
            - [实例0](#实例0)

<!-- /TOC -->

---

## 今日培训内容

[培训内容](https://gitee.com/thc1234/newbie/blob/master/now/note_day01.md)

---

## Debian 9.4.0 安装

1. (Virtubox on Linux)Virtubox需要配置双网卡(系统安装前先设置双网卡可以避免手动设置)

2. 直接选择installer, 使用图形化安装器会稍微慢一些

3. 查看网络信息使用`ip a`指令

4. Virtubox需要配置双网卡(Virtubox on Linux)(系统安装前先设置双网卡可以避免手动设置)

5. 先安装SSH

6. 在sudoers文件里加入普通账户，在远程连接中输入`sudo su`切换到root账户(`visudo`指令， 将root那一行复制在下一行， 并将root改为普通用户的名字)

7. 更换国内源(中科大的源快一些)(配置文件的位置是`/etc/apt/sources.list`)

8. 安装VIM

---

## Linux基本命令

1. 简单的Linux命令

- `mkdir`创建空目录， `mkdir -p`以递归方式
- `cd`更改当前目录
- `ls` `ls -lh` 查看
- `mv`移动
- `cat`查看文件
- `echo`输出
- `find`比较消耗资源(不推荐)
- `locate`查找比较快, 消耗资源比较少
- `echo XXXXX > 文件`重定向
- `echo XXXXX >> 文件`追加
- `ps -e | grep ssh`
- `wget`下载 `-C`断点下载
- `alias A=＇B＇`把Ｂ指令命名为Ａ
- `source`更新配置文件
- `pwd`查看绝对路径(前面没有左斜杠)
- `rm` 删除(小心手滑)
- `grep`文本搜索工具

2. 添加环境

- `export PATH=$PATH:/.../...`
- `alias`

3. vim基本操作

- 正常模式：`连续输入两个小写d` 删除当前的一行，　`输入一个大写Ｄ` 把光标在该行后面的内容删除，`输入一个小写ｐ`　复制该行到下一行
- 插入模式：`a` `i` `o` `大写G`在末尾插入
- 命令模式：`:XXX`, `:ｗq`保存并退出

---

## Node.js环境搭建

- git clone https://github.com/cnpm/nvm.git
- 在`bashrc`中加入`source /XX/XX/nvm/nvm.sh`
- `source ~/.bashrc`
- `nvm`
(有了nvm之后可以安装node.js的任意版本)
- `nvm install 10.5.0`下载node.js 10.5.0版本

---

## mongodb数据库

- `sudo apt-get install mongodb`
- `sudo apt-get install tmux`
- `mkdir XXX`为数据库创建一个文件夹
- `systemctl disable mongodb`
- `tmux`进入一个新的终端
- 在这个新的终端输入`mongod --dbpath /home/db`
- `Ctrl + D`回到原来的终端
- `mongo`
- `show dbs`查看存储情况
- `use 数据库名`使用数据库
- `db.数据集合名.instert({"XXX":"XXX"})`插入数据(增)
- `db.数据集合名.find()`查看当前数据库的信息
- `db.数据集合名.drop()`删除指定的数据集合(删)
- `db.dropDatabase()`删库
- `db.数据集合名.update({...})`改
- `db.数据集合名.findOne({...})`查

---

## Python双版本的配置

- 

---

## 晚上自习

### 输出Python3关键字

```python
import keyword
keyword.kwlist
```

### 注释

> 以`#`开头, 或者用`头尾的'''/"""`(类似于markdown的大代码框)

实例
```python
#!/usr/bin/python3

# 第一个注释
print("Hello, Python3!") # 第二个注释
```

```python
#!/usr/bin/python3

# 第一个注释
# 第二个注释

'''
第三注释
第四注释
'''

"""
第五注释
第六注释
"""
print("Hello, Python3!")
```
### 行与缩进

- <font color="dc143c">Python使用缩进来表示代码块, 不需要使用大括号`{}`. 缩进的空格数是可变的, 但是同一个代码块的语句必须包括相同的缩进空格数.</font>

### 多行语句

- 使用`\`右斜杠来实现多行语句

演示
```python
total = item_one + \
        item_two + \
        item_three
```

- 在[], {}, 或()中的多行语句, 不需要使用右斜杠`\`

演示
```python
total = ['item_one', 'item_two', 'item_three', 'item_four', 'item_five']
```

### 数字类型(number)

- int(整数), 只有一种整数类型int, 表示为长整型
- bool(布尔), 如True
- float(浮点数), 如1.23, 3E-2
- complex(负数), 如1+2j, 1.1+2.2j

### 字符串(string)

- Python中使用单引号和双引号完全相同
- 使用三引号(`'''`或`"""`)可以指定一个多行字符串
- 转义符'\'
- 反斜杠可以用来转义, 使用r可以让反斜杠不发生转义. 如`r"this is a line with \n"`, \n会显示, 并不是换行符.
- 按字面意思级联字符串, 如`"this"` `"is"` `"string"`会被自动转换成`this is string`
- 字符串可以使用`+`运算符连接在一起, 用`*`运算符重复
- Python中的字符串有两种索引方式, 从左往右以0开始, 从右往左以-1开始.
- Python中的字符串不能改变.
- Python没有单独的字符类型, 一个字符就是长度为1的字符串.
- 字符串的截取的语法格式如下: `变量[头下标:尾下标]`

演示
```python
word = '字符串'
sentence = "这是一个句子"
paragraph ="""这是一个段落,
可以由多行组成"""
```

#### 实例0
```python
#!/usr/bin/python3

str='Runoob'

print(str) #输出字符串
print(str[0:-1]) # 输出第一个到倒数第二个的所有字符
print(str[0]) # 输出字符串第一个字符
print(str[2:5]) # 输出第三个开始到第五个字符的字符
print(str[2:]) # 输出从第三个开始的后的所有字符
print(str * 2) # 输出字符串连续两次
print(str + '你好') # 连接字符串

print('----------------------')

print('hello\nrunoob') # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob') # 在字符串前面添加一个 r , 表示原始字符串, 不会发生转义
```