Python 3.12.4 (v3.12.4:8e8a4baf65, Jun  6 2024, 17:33:18) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#loops
#repetition
#DRY  - Dont Repeat Yourself
for i in range(1,11):
    print(i)

1
2
3
4
5
6
7
8
9
10
for i in range(1,11,2):
    print(i)

1
3
5
7
9

for i in range(1,11,-1):
    print(i)

for i in range(10,0,-1):
    print(i)

10
9
8
7
6
5
4
3
2
1

for i in reversed(range(1,11)):
    print(i)

10
9
8
7
6
5
4
3
2
1
#break statement
#it is used to go outside the loop
for i in range(1,1000000000):
    print(i)
    if i>10:
        break

1
2
3
4
5
6
7
8
9
10
11
#continue
for i in range(1,11):
    if i%2==0:
        continue
    print(i)
    print(*)
...     
SyntaxError: Invalid star expression
>>> for i in range(1,11):
...     if i%2==0:
...         continue
...     print(i)
...     print("*")
... 
1
*
3
*
5
*
7
*
9
*
