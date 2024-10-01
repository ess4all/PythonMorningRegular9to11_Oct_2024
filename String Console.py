Python 3.12.4 (v3.12.4:8e8a4baf65, Jun  6 2024, 17:33:18) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
x = 12
type(x)
<class 'int'>
x = 12.435
type(x)
<class 'float'>
#complex number
x = 1+2j
type(x)
<class 'complex'>
x.real
1.0
x.imag
2.0
x
(1+2j)
y = 2-3j
x+y
(3-1j)
x-y
(-1+5j)
x*y
(8+1j)
x/y
(-0.30769230769230776+0.5384615384615384j)
-4/13
-0.3076923076923077
#String
#String - >collections of character
x = 'a'
type(x)
<class 'str'>
x = 'hello'
type(x)
<class 'str'>
x = "hello"
type(x)
<class 'str'>
x = '"Python" is easy to learn'
print(x)
"Python" is easy to learn
x = "\"Python\" is easy to learn" #/-escape sequence

#INDEXING
x = "Lets Learn Python"
x[0]
'L'
x[-1]
'n'
x[-3]
'h'
#SLICING
x[0:4]
'Lets'
x[0:4:1]
'Lets'
x[-1:2,2]
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    x[-1:2,2]
TypeError: string indices must be integers, not 'tuple'
x[-1:2:2]
''
x[-1:1000]
'n'
x[-1:1000:2]
'n'

x[1:5]#ending - n-1
'ets '
x[10,1,-1]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    x[10,1,-1]
TypeError: string indices must be integers, not 'tuple'
x[5:1:-1]
'L st'
x
'Lets Learn Python'
#ending - n+1
x
'Lets Learn Python'
x[-1:2]
''
x[1:5:-1]
''
x
'Lets Learn Python'
x[:-1]
'Lets Learn Pytho'
x
'Lets Learn Python'
x.upper()
'LETS LEARN PYTHON'
x.lower()
'lets learn python'
x.capitalize()
'Lets learn python'
x.title()
'Lets Learn Python'
#String - immutable
x
'Lets Learn Python'
x.isalpha()
False
x = "5435retgf"
x.isalnum()
True
x= "345"
x.isdigit()
True
x
'345'
x = "hello"
x.isupper()
False
x
'hello'
x = "Welcome to Python Programming"
x.find("o")
4
x.rfind("o")
20
x.find("o")
4
x.find("o",0)
4
x.find("o",5)
9
x.index("o",5)
9
x.find("X")
-1
x.index("X")
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    x.index("X")
ValueError: substring not found

a

a = 12
b = 0
a/b
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    a/b
ZeroDivisionError: division by zero
x
'Welcome to Python Programming'
x.count("o")
4
x.split()
['Welcome', 'to', 'Python', 'Programming']

import webbrowser
x = "open google"
x.split()
['open', 'google']
webbrowser.open("https://"+x.split()[1]+".com")
True

x = 'Welcome to Python Programming'
x.split("o")
['Welc', 'me t', ' Pyth', 'n Pr', 'gramming']
x
'Welcome to Python Programming'
x = '''
Features of Python:
High Level
General Purpose
Interpreted'''
x.splitlines()
['', 'Features of Python:', 'High Level', 'General Purpose', 'Interpreted']
len(x.splitlines())
5
x
'\nFeatures of Python:\nHigh Level\nGeneral Purpose\nInterpreted'
len(x)
59
x = 'Welcome to Python Programming'
x = x.split()
x
['Welcome', 'to', 'Python', 'Programming']
" ".join(x)
'Welcome to Python Programming'
"####".join(x)
'Welcome####to####Python####Programming'
x = "python"
x.center(7)
' python'
x.center(20)
'       python       '
x.center(9)
'  python '
x.center(9,"*")
'**python*'
x = x.center(40,"*")
x
'*****************python*****************'
x.lstrip("*")
'python*****************'
x.rstrip("*")
'*****************python'
x.strip("*")
'python'
x = " *****pyt*h*n*******"
x.strip("*")
' *****pyt*h*n'
x
' *****pyt*h*n*******'
x.replace("*","")
' pythn'
#ORD & CHR
#ord - ordinal
#chr - character
ord("z")
122
chr(99)
'c'
x = 1
for i in range(0,6):
    print(chr(97+i))

a
b
c
d
e
f
>>> x = "abcdefghij"
>>> for i in x:
...     print(ord(i))
... 
97
98
99
100
101
102
103
104
105
106
>>> x = "python"
>>> x.zfill(20)
'00000000000000python'
