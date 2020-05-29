ch=int(input('Press 1.Unit 2. Temperature'))
if ch == 1:
    
    a=int(input('enter existing unit 1.CGS 2.MKS'))
    b=int(input('enter conv unit 1.CGS 2.MKS'))
    unit = float(input('enter value'))
    if (a == 1) & (b == 2):
        print(unit*1000)
    elif (a == 2) & (b == 1):
        print(unit/1000)

elif ch == 2:
    
    a=int(input('enter existing unit 1.C 2.F'))
    b=int(input('enter conv unit 1.C 2.F'))
    temp = float(input('temp'))
    if (a == 1) & (b == 2):
        print((9*temp)/5 +32)
    elif (a== 2) & (b == 1):
        print((temp-32)*5/9)
else :
    print('wrong option')
    
