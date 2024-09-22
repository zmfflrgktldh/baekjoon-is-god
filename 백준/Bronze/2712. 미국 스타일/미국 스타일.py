import math
a=[]
for i in range(int(input())):
    a=input().split()
    if a[1]=='kg':
        w=round(float(a[0])*2.2046,4)
        print(f'{w:0.4f} lb')
    if a[1]=='lb':
        w=round(float(a[0])*0.4536,4)
        print(f'{w:0.4f} kg')
    if a[1]=='l':
        w=round(float(a[0])*0.2642,4)
        print(f'{w:0.4f} g')
    if a[1]=='g':
        w=round(float(a[0])*3.7854,4)
        print(f'{w:0.4f} l')