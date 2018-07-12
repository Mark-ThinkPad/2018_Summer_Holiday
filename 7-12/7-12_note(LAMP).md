# 7.12.note

`Linux server built`

---

## Content

<!-- TOC -->

- [7.12.note](#712note)
    - [Content](#content)
    - [Debian 9.4.0 安装](#debian-940-安装)

<!-- /TOC -->

---

## Debian 9.4.0 安装

1. Virtubox需要配置双网卡(Virtubox on Linux)（系统安装前先设置双网卡可以避免手动设置）

2. 直接选择installer， 使用图形化安装器会稍微慢一些

3. 查看网络信息使用`ip a`指令

4. Virtubox需要配置双网卡(Virtubox on Linux)（系统安装前先设置双网卡可以避免手动设置）

5. 先安装SSH

6. 在sudoers文件里加入普通账户，在远程连接中输入`sudo su`切换到root账户（`visudo`指令， 将root那一行复制在下一行， 并将root改为普通用户的名字）

7. 更换国内源（中科大的源快一些）（配置文件的位置是`/etc/apt/sources.list`）

8. 安装VIM

