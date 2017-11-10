Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> y = '123@qq.comaaa@163.comasdfasfs3333@dfcom'
>>> import re
>>> y = '123@qq.comaaa@163.comasdfasfs3333@dfcom'
>>> re.findall('\w+@\w+.com',y)
['123@qq.com', 'aaa@163.com', 'asdfasfs3333@dfcom']
>>> 
>>> y = 'tel:010-12354678 address:changRoad'
>>> re.findall('d',y)
['d', 'd', 'd']
>>> re.findall('\d,y)
	   
SyntaxError: EOL while scanning string literal
>>> re.findall('\d',y)
['0', '1', '0', '1', '2', '3', '5', '4', '6', '7', '8']
>>> y = 'tel:010-12354678 address:changRoad tel:025-58887456'
>>> re.findall('\d{3,4}\d{7,8}',y)
[]
>>> re.findall('\d{3,4}-\d{7,8}',y)
['010-12354678', '025-58887456']
>>> re.findall('\d{7,8}',y)
['12354678', '58887456']
>>> re.findall('\d{3,4}',y)
['010', '1235', '4678', '025', '5888', '7456']
>>> re.findall('\d+',y)
['010', '12354678', '025', '58887456']
>>> 
