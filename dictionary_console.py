Python 3.12.4 (v3.12.4:8e8a4baf65, Jun  6 2024, 17:33:18) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#Tuple
#Tuple - Immutable
x = (1,2,3,4)
x.pop()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    x.pop()
AttributeError: 'tuple' object has no attribute 'pop'
x[0]=100
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    x[0]=100
TypeError: 'tuple' object does not support item assignment
x
(1, 2, 3, 4)
len(x)
4
sum(x)
10
min(x)
1
max(x)
4
x = (1,2,3,4,5,2,21,1,1,1,1)
x.count(1)
5
x.index(2)
1
#Dictionary
#Key:Value Pair
x = {"id":101,"name":"ravi","marks":90}
type(x)
<class 'dict'>
x
{'id': 101, 'name': 'ravi', 'marks': 90}
x["contact"]=9876543210
#adding key value pair
x
{'id': 101, 'name': 'ravi', 'marks': 90, 'contact': 9876543210}
#update
x["
  
SyntaxError: unterminated string literal (detected at line 1)

x
  
{'id': 101, 'name': 'ravi', 'marks': 90, 'contact': 9876543210}
x["name"]="Rahul"
  
x
  
{'id': 101, 'name': 'Rahul', 'marks': 90, 'contact': 9876543210}
x.popitem()#removing last key value pair
  
('contact', 9876543210)
x
  
{'id': 101, 'name': 'Rahul', 'marks': 90}
x.pop("name")
  
'Rahul'
x
  
{'id': 101, 'marks': 90}
del x["id"]
  
x
  
{'marks': 90}
x.clear()
  
x
  
{}
x={'id': 101, 'name': 'Rahul', 'marks': 90, 'contact': 9876543210}
  
x
  
{'id': 101, 'name': 'Rahul', 'marks': 90, 'contact': 9876543210}
x.keys()
  
dict_keys(['id', 'name', 'marks', 'contact'])
x.values()
  
dict_values([101, 'Rahul', 90, 9876543210])
x.items()
  
dict_items([('id', 101), ('name', 'Rahul'), ('marks', 90), ('contact', 9876543210)])
x
  
{'id': 101, 'name': 'Rahul', 'marks': 90, 'contact': 9876543210}
len(x)
  
4
x
  
{'id': 101, 'name': 'Rahul', 'marks': 90, 'contact': 9876543210}
#Dictionary is unordered
  
x["id"]
  
101
x["contact"]
  
9876543210
x
  
{'id': 101, 'name': 'Rahul', 'marks': 90, 'contact': 9876543210}
x.get("id")
  
101
