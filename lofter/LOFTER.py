import urllib 
import urllib2
import re  
  
class Spider:  
    def __init__(self,url): 
        self.url=url  
    def getPage(self):  
        url = self.url  
        requests = urllib2.Request(url)  
        response = urllib2.urlopen(requests)  
        return response.read() 
url = 'http://yangxiaomingmasato.lofter.com/' 
spider = Spider(url)
content = spider.getPage() 
pattern = re.compile('<div class="pic.*?<a class="img" href=.*?<img src="(.*?)"',re.S)
picUrls = re.findall(pattern,content)
print len(picUrls)
num = 1  
for picUrl in picUrls:  
        pic = urllib.urlopen(picUrl)
        picData = pic.read() 
        picFile = open('pic-'+str(num)+'.jpg','wb')  
        picFile.write(picData)
        picFile.close()  
        num +=1  

