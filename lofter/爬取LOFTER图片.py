import urllib  
import urllib2#����urllib2��  
import re  
  
class Spider:#����һ��������  
    def __init__(self,url):#���캯�����г�ʼ�����ڶ�������������Ҫץ����ҳurl  
        self.url=url  
    def getPage(self):#��ȡ��ҳ���ݵķ���  
        url = self.url  
        requests = urllib2.Request(url)#����Requestʵ��  
        response = urllib2.urlopen(requests)  
        return response.read()#��ȡ��õ���ҳ����  
url = 'http://yangxiaomingmasato.lofter.com/'#Ŀ����ҳ�ĵ�ַ  
spider = Spider(url)#����һ������ʵ��  
content = spider.getPage()#���Ŀ����ҳ����  
pattern = re.compile('<div class="pic.*?<a class="img" href=.*?<img src="(.*?)"',re.S)#��������ͼƬ��ַ��ʽ��������ʽ  
picUrls = re.findall(pattern,content)#����ҳ�����в�ѯ����Ҫ����ַ���  
print len(picUrls)#��һ��ץ����������Ҫ��ĵ�ַ  
num = 1  
for picUrl in picUrls:  
        pic = urllib.urlopen(picUrl)#��ͼƬ��ַ  
        picData = pic.read()#��ȡͼƬ����  
        picFile = open('pic-'+str(num)+'.jpg','wb')#�򿪱���ͼƬ�ļ�  
        picFile.write(picData)#д��ͼƬ����  
        picFile.close()#�ر��ļ�  
        num +=1  

