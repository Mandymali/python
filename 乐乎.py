import urllib2
import urllib
import re

#声明一个爬虫类
class Spider:
    def __init__(self,url):#构造函数进行初始化，第二个参数使我们要抓取得网页url
        self.url=url
    #获取网页内容的方法
    def getpage(self):
        url = self.url
        #构造request实例
        requests = urllib2.Request(url)
        response = urllib2.urlopen(requests)
        #读取获得的网页内容
        return response.read()
#目标网页的地址
url = 'http://noisewoo.lofter.com/'
#创建一个爬虫实例
spider = Spider(url)
#获得目标网页内容
content = spider.getpage()
#创建符合图片地址格式的正则表达式
pattern = re.compile('<img src="(.*?)"',re.S)
picurls = re.findall(pattern,content)#在网页内容中查询符合要求的字符串

print len(picurls)#看一下抓到几个符合要求的地址
num = 1
for picurl in picurls:
    #print(picurl)
    #pic = urllib.urlopen(picurl)#打开图片网址
    #picData = pic.read()#获取图片数据
    picFile = "D:/jsl/Python/" + str(num)+".jpg"#打开本地图片文件
    urllib.urlretrieve(picurl,filename=picFile)#写入数据
    num +=1
    
    #print picurl

