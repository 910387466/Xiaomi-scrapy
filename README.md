### Xiaomispider
* [爬取小米市场的网址](http://app.mi.com/topList)

* python

* 实现了多页爬取

* 写入文件json

* 爬取apk保存到本地

缺点 ：下载时会阻断，就会导致下载的效率不是很高。
       下载部分代码为用的python的urllib来下载的，自己研究scrapy的下载没有成功，里面的results没有任何东西。懂得大神可以教教我哟。
       
这个为最近工作需要，时间紧迫所临写的，目的为下载小米市场的应用，使用后发现scrapy这个爬虫框架真心的高大上。
代码中也要部分的注释，使用时看看就会懂。
 
### 在scrapy中多页爬取有三中策略。
1
```
start_urls = ['http://app.mi.com/topList?page=%s' %n for n in xrange(1,4)] //通过在初始爬取中循环来实现多页爬取
```
2
```
if newxia:#下一页
    newxiayiye = self.start_urls[0]+newxia.encode('utf-8')
    yield scrapy.Request(newxiayiye,callback=self.parse_S)
else:
    pass   //通过判断网页上下一页来实现多页爬取
```
3
```
rules = (
        Rule(LinkExtractor(allow=(r'http://app\.mi\.com/topList\?page=\d+.*')),callback='parse_S'),
        )   //通过调用scrapy的内置方法LinkExtractor,来实现多页爬取，具体的使用请自行查找【注意这个方法是从网页上静态的获取，无法获取像1 2 3 4 ... 20 。
```
 
### 使用
 修改后setting中的FILES_STORE ，实现自己的下载路径
 
```
 scrapy crawl xiaomi  //或者 scrapy  crawl xiaomi -L WARNING  为不输出log内容，只输出自定义的输出。
 
 scrapy crawl xiaomi -s LOG_FILE=scrapy.log   //将log内容保存到文件。
 
 scrapy crawl xiaomi -o name.json    //【o 字母不是数字】在命令行中输出json数据，一般用在初步验证程序的正确性，谨慎使用为数据的最终输出结果。

```
 
### JSON中保存的内容

* 应用的名称

* 软件大小

* 版本

* 分类

* 包名

* 更新时间

* 公司

* appid

* 下载地址

* 评价

* 权限详情

该为临时的爬虫，会进行改进，__本人新手，大神勿喷__。

