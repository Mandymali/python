import urllib2
import urllib
import re

#����һ��������
class Spider:
    def __init__(self,url):#���캯�����г�ʼ�����ڶ�������ʹ����Ҫץȡ����ҳurl
        self.url=url
    #��ȡ��ҳ���ݵķ���
    def getpage(self):
        url = self.url
        #����requestʵ��
        requests = urllib2.Request(url)
        response = urllib2.urlopen(requests)
        #��ȡ��õ���ҳ����
        return response.read()
#Ŀ����ҳ�ĵ�ַ
url = 'http://noisewoo.lofter.com/'
#����һ������ʵ��
spider = Spider(url)
#���Ŀ����ҳ����
content = spider.getpage()
#��������ͼƬ��ַ��ʽ��������ʽ
pattern = re.compile('<img src="(.*?)"',re.S)
picurls = re.findall(pattern,content)#����ҳ�����в�ѯ����Ҫ����ַ���

print len(picurls)#��һ��ץ����������Ҫ��ĵ�ַ
num = 1
for picurl in picurls:
    #print(picurl)
    #pic = urllib.urlopen(picurl)#��ͼƬ��ַ
    #picData = pic.read()#��ȡͼƬ����
    picFile = "D:/jsl/Python/" + str(num)+".jpg"#�򿪱���ͼƬ�ļ�
    urllib.urlretrieve(picurl,filename=picFile)#д������
    num +=1
    
    #print picurl

