#You have 3 Sides , if they can form a traingle....
#which traingle it is ? equilateral/isoceles/scalene

x = int(input("Please enter First side:"))
y = int(input("Please enter Sec side:"))
z = int(input("Please enter Third side:"))


if x==y==z:
    print("This is Equilateral")
elif x==y or y==z or z==x:
    print("This is Isoceles")
else:
    print("This is Scalene")










