#find the sum of fist 10 natural nos
'''
res = 0
for i in range(1,11):
    res = res+i
print(res)
'''
#check whether a no is prime or not
'''
x= int(input("Enter No : "))
for i in range(2,x):
    if x%i==0:
        print(f"{x} is not prime")
        break
else:
    print("Prime")
'''
#FInd the sum of digits of number
# 125 -> 1+2+5->8
'''
res = 0
x = int(input("Please enter your digit:"))
for i in range(len(str(x))):
    digit = x%10
    res = digit + res*10
    x= x//10
print(res)
'''

#Nested For Loop
#print prime nos b/w 1to100
'''
for each in range(1,101):
    for i in range(2,each):
        if each%i==0:
            break
    else:
        print(each)  
'''
'''
    *
   **
  ***
 ****
*****
for i in range(1,6):
    print("*"*i)

'''
'''
for i in range(1,6):
    print(" "*(5-i)+"*"*i)
'''

'''
1
12
123
1234
12345

1
22
333
4444
55555

1
01
010
1010
10101
'''
'''
for i in range(1,6):
    # col
    for j in range(i):
        print(j,end="")
    print()
    '''

# row
'''
for i in range(1,6):
    # col
    for j in range(i):
        print("*",end="")
    print()
'''
'''
for i in range(1,11):
    print(i,end=",")
'''

'''
for each in range(1,6):
    for i in range(1,6):
        print(i,end="")
   
   '''
'''
x = 1
for i in range(1,6):
    # col
    for j in range(0,i):
        if (x%2) == 0:
            print("0",end="")
        else:
            print("1",end="")    
            #print(x,end="")
        x = x+1
    print()
'''
'''
*   *
*   *
*****
*   *
*   *
for i in range(1,6):
    for j in range(1,6):
        if j in (1,5) or i==3:
            print("*",end="")
        else:
            print(" ",end="")
    print()
'''
'''
for i in range(1,8):
    for j in range(1,6):
        if i in (1,4,7) or (j == 1) or (j==5):
            if (j==5) and i in (1,4,7):
                print(" ",end="")
            else:
                print("*",end="")
        else:
            print(" ",end="")
    print()


'''
'''
for i in range(1,8):
    for j in range(1,6):
        if i in (1,4) or (j == 1) or (j==5):
            if (i==1) and j in (1,5):
                print(" ",end="")
            else:
                print("*",end="")
        else:
            print(" ",end="")
    print()

'''
'''
for i in range(1,8):
    for j in range(1,8):
        if i in (1,7) or i== 8-j:
            print("*", end="")
        else:
            print(" ", end="")
    print()        


'''
for i in range(1,8):
    for j in range(1,6):
        if i in (1,4) or j in (1,5) :
            if (j==1 or i in (1,4)) or (j==5 and i in (2,3,7)):
                if i in (1,4) and j==5:
                    print(" ",end="")
                else:
                   print("*",end="")
            elif j==5 and i in (1,4):
                print(" ",end="")
            else:
                print(" ",end="")
        elif i==j+2 :
            print("*",end="")
        else:
            print(" ",end="")
    print()






