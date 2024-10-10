# 1. Find largest no from the List
# 2. Find Second largest no from the List
# 3. take a no as input and check whether the no is present 
#    in the list or not
# 
# 
# '''
'''
x=[1,20000000,3,4,5,6,7,8,9,101]
large = x[0]
for i in range(1,len(x)):
    if x[i]>large:
        large = x[i]
print(large)



x=[1,20000000,3,4,5,6,7,8,9,101]
large = x[0]
seclarge = x[1]
for i in range(1,len(x)):
    if x[i]>large:
        seclarge = large
        large = x[i]
    elif x[i]>seclarge:
        seclarge = x[i]

print(large)
print(seclarge)
'''

'''
x = [1,90,98,909,987665,96654,2,34549594,9865,2836]
lar = x[0]
seclar = x[1]
for i in range(1,len(x)):
    if x[i]>lar:
        seclar = lar
        lar = x[i]
    elif x[i]>seclar:
        seclar = x[i]

print(lar)   
print(seclar) 


x=int(input("Please enter your number:"))
y = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


if x in y:
    print('found')
else:
    print("Not found")

for i in y:
    if x==i:
        print("found")
        break
else:
    print("Not Found..")


#4.Sort the List in Ascending order.

x=[1,-202,534,56,78,98,909]
y=[]
for i in range(0,len(x)-1):
    for j in range(i+1,len(x)):
        if x[i]>x[j]:
            x[i],x[j]=x[j],x[i]

print(x)
'''

# x=[1,2,3,4]
# last = x[-1]
# for i in reversed(range(len(x))):
#     x[i]=x[i-1]
# x[0]=last
# print(x)

y = []

import random
for i in range(5):
    random.randint(1,5)





