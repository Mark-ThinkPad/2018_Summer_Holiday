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