/**
 * 需求分析
 *    1. 数据获取
 *      1.1 URL = https://route.showapi.com/181-1?showapi_appid=30603&showapi_sign=98960666afeb4992ae91971d13494090&page=1&num=8
 *      1.2 ajax
 *        1.2.1 创建xhr对象
 *        1.2.2 开启数据通道
 *        1.2.3 提交请求
 *        1.2.4 监听数据通道变化    
 *    2. 数据渲染dom  
 *      2.1 获取dom节点
 *        2.1.1 querySelector 
 *        2.1.2 querySelectorAll
 *      2.2 模板渲染  
 *        2.2.1 es6 模板字符串
 *    3. 分页业务实现
 *        3.1 事件委托 -> 事件冒泡
 *        3.2 for in 遍历
 *        3.3 数组操作  join push   
 *    4. 缓存代理业务实现
 *        4.1 缓存池  -> 对象
 *        4.2 对象的存取操作  -> . 和 [] 的区别
 */

 const URL = "https://route.showapi.com/181-1?";
 var oCon = document.querySelector('.content');
 var oUl = document.querySelectorAll('.flex_row')[0];
 var page = 1;

 var cache = {}; // 缓存池

 function getXhr(){
    if(window.XMLHttpRequest){
        return new XMLHttpRequest();
    }else{
        return new ActiveXObject('Microsoft.XMLHTTP'); // IE6以及IE6以下浏览器
    }
 }

 oUl.addEventListener('click', function(e){
    console.log(e);
    if(e.target.tagName.toLowerCase() === "li"){
        page = e.target.innerHTML;
        if(page in cache){
            console.log('数据已经缓存,页码:'+page);
            showPage(cache[page]);
        }else{
            getData();
        }
    }
 }, false)
 
 getData();
 function getData(){
    console.time('正在拉取数据');
    var xhr = getXhr();
    var params = []; // 中转数组
    var sendData = {
        'showapi_appid': '30603',
        'showapi_sign': '98960666afeb4992ae91971d13494090',
        'page': page,
        'num': 8
    }
    for(var key in sendData){
        params.push(key + '=' + sendData[key]);
    }
    var postData = params.join('&');
    xhr.open("GET", URL+postData, true);
    xhr.send(null);
    xhr.onreadystatechange = function(){
        if(xhr.readyState == 4 && xhr.status == 200){
            // console.log(JSON.parse(xhr.responseText).showapi_res_body.newslist);
            var dataList = JSON.parse(xhr.responseText).showapi_res_body.newslist;
            cache[page] = dataList; // 缓存数据
            showPage(dataList);
        }
    }
 }
 
 function showPage(data){
    console.log(data)
    var len = data.length;
    var str = '';
    for(var i=0; i<len; i++){
        str += `
        <a href="${data[i].url}" class="items flex_row load">
            <div class="img"><img src="${data[i].picUrl}" alt=""></div>
            <div class="bd">
                <p class="label">${data[i].title}</p>
            </div>
            <div class="ft">&GT;</div>
        </a>
        `
    } 
    oCon.innerHTML = str;
    console.timeEnd('正在拉取数据');
 }