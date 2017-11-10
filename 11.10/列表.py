Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> var = '1'
>>> print type(var)
<type 'str'>
>>> n_var = int(var)+1
>>> print n_var
2
>>> var = 'abc'
>>> int(var)

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(var)
ValueError: invalid literal for int() with base 10: 'abc'
>>> page_num = 1
>>> print "第",page_num,"页"
第 1 页
>>> print type(page_num)
<type 'int'>
>>> print "第" + str(page_num) + "页"
第1页
>>> print random()

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print random()
NameError: name 'random' is not defined
>>> import random
>>> random.Random()
<random.Random object at 0x0201CE30>
>>> random.choice("['a','b','c']")
'b'
>>> random.choice("['a','b','c']")
"'"
>>> random.choice("['a','b','c']")
"'"
>>> test_list = ['a','b','c']
>>> random.choice(test_list)
'a'
>>> rendom.choice("['a','b','c']")

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    rendom.choice("['a','b','c']")
NameError: name 'rendom' is not defined
>>>  rendom.choice("['a','b','c']")

  File "<pyshell#19>", line 2
    rendom.choice("['a','b','c']")
    ^
IndentationError: unexpected indent
>>> random.choice(['a','b','c'])
'b'
>>>  random.choice(['a','b','c'])
 
  File "<pyshell#21>", line 2
    random.choice(['a','b','c'])
    ^
IndentationError: unexpected indent
>>> random.choice(['a','b','c'])
'c'
>>> random.choice(['a','b','c'])
'b'
>>> random.choice(['a','b','c'])
'a'
>>> random.choice(['a','b','c'])
'a'
>>> random.choice(['a','b','c'])
'a'
>>> random.choice(['a','b','c'])
'b'
>>> random.choice(['a','b','c'])
'c'
>>> 
>>> list1 = ['physics','chemistry',1997,2000]:
	
SyntaxError: invalid syntax
>>> list1 = ['physics','chemistry',1997,2000];
>>> list1[0]
'physics'
>>> list1[1]
'chemistry'
>>> list1[0:1]
['physics']
>>> list1[0:2]
['physics', 'chemistry']
>>> list1[1:3]
['chemistry', 1997]
>>> list2 = [1,2,3,4,5];
>>> list1 + list2
['physics', 'chemistry', 1997, 2000, 1, 2, 3, 4, 5]
>>> list1=[2,4]
>>> list1 *2
[2, 4, 2, 4]
>>> list2 *2
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
>>> 
>>> 3 in [1,2,3]:
	
SyntaxError: invalid syntax
>>> 3 in [1,2,3]
True
>>> if 2 in [1,2,3]:
	print OK

	

Traceback (most recent call last):
  File "<pyshell#49>", line 2, in <module>
    print OK
NameError: name 'OK' is not defined
>>> if 3 in [1,2,3]:
	print "OK"

	
OK
>>> list = []
>>> list.append("a")
>>> list
['a']
>>> list = ['physics','chemistry',1997,2000]:
	
SyntaxError: invalid syntax
>>> list = ['physics','chemistry',1997,2000];
>>> list[2]
1997
>>> list[2] = 2001
>>> list
['physics', 'chemistry', 2001, 2000]
>>> del list[2]
>>> list
['physics', 'chemistry', 2000]
>>> list1
[2, 4]
>>> list2
[1, 2, 3, 4, 5]
>>> cmp(list1,list2)
1
>>> list1 = [2,3,4,5,6]
>>> cmp(list1,list2)
1
>>> list1 = [0,1]
>>> cmp(list1,list2)
-1
>>> list1,list2 = [123,'zuy'],[456,'adf']
>>> cmp(list1,list2)
-1
>>> list1 = [789,'zzz']
>>> cmp(list1,list2)
1
>>> len(list1)
2
>>> list2 = [1,2,3,4,5]
>>> max(list2)
5
>>> tuple1 = (1,2,3,4)
>>> list(tuple1)

Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    list(tuple1)
TypeError: 'list' object is not callable
>>> aTuple = (124,'zuy','zaol','ad')
>>> aList = list(aTuple)

Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    aList = list(aTuple)
TypeError: 'list' object is not callable
>>> list2
[1, 2, 3, 4, 5]
>>> list2.reverse()
>>> list2
[5, 4, 3, 2, 1]
>>> 
