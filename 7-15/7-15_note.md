# 2018.7.15 note

---

## Content

<!-- TOC -->

- [2018.7.15 note](#2018715-note)
    - [Content](#content)
    - [先把昨天写的爬虫封装成一个函数](#先把昨天写的爬虫封装成一个函数)

<!-- /TOC -->

---

## 先把昨天写的爬虫封装成一个函数

---

```
var jquery = document.createElement('script');  
jquery.src = "http://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js";//若调试页面是https的这里也修改为https.
document.getElementsByTagName('head')[0].appendChild(jquery);  
jQuery.noConflict();

$.post("http://0.0.0.0/api/info",
    {
      username:"201703407",
      password:"201703407"
    },
    function(data,status){
      thc = data;
    });
```

有效代码!!!
```
$.post("http://0.0.0.0/api/info",
    {
      username:"201703407",
      password:"201703407"
    },
    function(data,status){
      thc = $.parseJSON(data);
    });
```