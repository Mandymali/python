import urllib2
import urllib
import re

class Spider:
    def __init__(self,url):
        self.url=url
   
    def getpage(self):
        url = self.url
  
        requests = urllib2.Request(url)
        response = urllib2.urlopen(requests)
     
        return response.read()

url = 'http://noisewoo.lofter.com/'

spider = Spider(url)

content = spider.getpage()

pattern = re.compile('<img src="(.*?)"',re.S)
picurls = re.findall(pattern,content)

print len(picurls)
num = 1
for picurl in picurls:
    #print(picurl)
    #pic = urllib.urlopen(picurl)
    #picData = pic.read()
    picFile = "D:/jsl/Python/" + str(num)+".jpg"
    urllib.urlretrieve(picurl,filename=picFile)
    num +=1
    
    #print picurl

