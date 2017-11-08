Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> line = "Cats are smarter than dogs"
>>> line
'Cats are smarter than dogs'
>>> import re
>>> re.match(r'dogs',line,re.M|re.I)
>>> re.match(r'Cats',line,re.M|re.I)
<_sre.SRE_Match object at 0x01659988>
>>> matchObje = re.match(r'Cats',line,re.M|re.I)
>>> matchObje.group()
'Cats'
>>> matchObje = re.search(r'dogs',line,re.M|re.I)
>>> print matchObje.group()
dogs
>>> matchObje = re.search(r'Dogs',line,re.M|re.I)
>>> print matchObje.group()
dogs
>>> matchObje = re.search(r'Dogs',line,re.M)
>>> print matchObje.group()

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print matchObje.group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> matchObj

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    matchObj
NameError: name 'matchObj' is not defined
>>> matchObje
>>> line = "Cats are smarter than dogs"
>>> matchObje = re.search(r'dogs',line)
>>> matchObje
<_sre.SRE_Match object at 0x0206B1A8>
>>> matchObje = re.search(r'dogs$',line)
>>> matchObje
<_sre.SRE_Match object at 0x0206B1E0>
>>> matchObje.group()
'dogs'
>>> line = "Cats are dogs smarter than dogs"
>>> matchObje = re.search(r'dogs$',line)
>>> matchObje.group()
'dogs'
>>> 
