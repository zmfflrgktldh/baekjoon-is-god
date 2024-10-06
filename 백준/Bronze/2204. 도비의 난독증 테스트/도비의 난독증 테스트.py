a=[]
b=''
c=[]
while True:
    b=(int(input()))
    if b==0:
        break
    c=[]
    a=[]
    for i in range(b):
        b=input()
        c.append(b)
        a.append(b.lower())
    print(c[a.index(sorted(a)[0])])