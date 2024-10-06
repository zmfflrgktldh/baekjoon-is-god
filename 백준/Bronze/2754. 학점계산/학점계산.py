score=input()
result=0
if 'A' in score:
    result+=4
elif 'B' in score:
    result+=3
elif 'C' in score:
    result+=2
elif 'D' in score:
    result+=1
else:
    result+=0
if '+' in score:
    result+=0.3
elif '-' in score:
    result-=0.3
else:
    result+=0.0
print(result)