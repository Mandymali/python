Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib
>>> import urllib2
>>> url = 'http://www.zhihu.com/'
>>> user_agent ='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:0.9.4) Gecko/20011128 Netscape6/6.2.1'
>>> headers ={ 'User_Agent' : user_agent }
>>> request = urllib2.Request('http://www.zhihu.com/',headers={'User_Agent' : user_agent })
>>> response = urllib2.urlopen(request)
>>> page = response.read()
>>> 
