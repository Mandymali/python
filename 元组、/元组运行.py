Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> tup1 = ('physics','chemistry',1997,2000);
>>> tup2 = (1,2,3,4,5,6,7);
>>> print "tup1[0]:",tup1[0]
tup1[0]: physics
>>> print "tup2[1:5]:",tup2[1:5]
tup2[1:5]: (2, 3, 4, 5)
>>> 
========== RESTART: D:/网络163 姜圣玲/python/py/元组、/访问元组.py ==========
tup1[0]:  physics
tup2[1:5]:  (2, 3, 4, 5)
>>> 
========== RESTART: D:/网络163 姜圣玲/python/py/元组、/修改元组.py ==========
(12, 34.56, 'abc', 'xyz')
>>> 
========== RESTART: D:/网络163 姜圣玲/python/py/元组、/删除元组.py ==========
('physics', 'chemistry', 1997, 2000)
After deleting tup : 

Traceback (most recent call last):
  File "D:/网络163 姜圣玲/python/py/元组、/删除元组.py", line 8, in <module>
    print tup;
NameError: name 'tup' is not defined
>>> 
========== RESTART: D:\网络163 姜圣玲\python\py\元组、\访问元组.py ==========
tup1[0]:  physics
tup2[1:5]:  (2, 3, 4, 5)
('physics', 'chemistry', 1997, 2000)
After deleting tup : 

Traceback (most recent call last):
  File "D:\网络163 姜圣玲\python\py\元组、\访问元组.py", line 12, in <module>
    print tup;
NameError: name 'tup' is not defined
>>> 
========== RESTART: D:/网络163 姜圣玲/python/py/元组、/删除元组.py ==========
('physics', 'chemistry', 1997, 2000)
After deleting tup : 

Traceback (most recent call last):
  File "D:/网络163 姜圣玲/python/py/元组、/删除元组.py", line 8, in <module>
    print tup;
NameError: name 'tup' is not defined
>>> 
======== RESTART: D:/网络163 姜圣玲/python/py/元组、/无关闭分隔符.py ========
abc -4.24e+93 (18+6.6j) xyz
Value of x , y :  1 2
>>> 
>>> 
>>> L = ('spam','Spanm','ASDas!')
>>> L[2]
'ASDas!'
>>> L[-2]
'Spanm'
>>> L[1:]
('Spanm', 'ASDas!')
>>> 
>>> 
>>> tup1 = ("all")
>>> print tup1
all
>>> tup1 = ("all",)
>>> print tup1
('all',)
>>> 
