import urllib  
import urllib2#引入urllib2库  
import re  
  
class Spider:#声明一个爬虫类  
    def __init__(self,url):#构造函数进行初始化，第二个参数是我们要抓的网页url  
        self.url=url  
    def getPage(self):#获取网页内容的方法  
        url = self.url  
        requests = urllib2.Request(url)#构造Request实例  
        response = urllib2.urlopen(requests)  
        return response.read()#读取获得的网页内容  
url = 'http://yangxiaomingmasato.lofter.com/'#目标网页的地址  
spider = Spider(url)#创建一个爬虫实例  
content = spider.getPage()#获得目标网页内容  
pattern = re.compile('<div class="pic.*?<a class="img" href=.*?<img src="(.*?)"',re.S)#创建符合图片地址格式的正则表达式  
picUrls = re.findall(pattern,content)#在网页内容中查询符合要求的字符串  
print len(picUrls)#看一下抓到几个符合要求的地址  
num = 1  
for picUrl in picUrls:  
        pic = urllib.urlopen(picUrl)#打开图片网址  
        picData = pic.read()#读取图片数据  
        picFile = open('pic-'+str(num)+'.jpg','wb')#打开本地图片文件  
        picFile.write(picData)#写入图片数据  
        picFile.close()#关闭文件  
        num +=1  

