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

- 插入模式：`a` `i` `o`
 
- 命令模式：`:XXX`, `:ｗq`保存并退出

---

## Node.js环境搭建

