
#ZeroDivisionError Handling
while True:
    num = int(input('enter num'))
    dem=  int(input('enter dem'))
    if dem ==1:
        break
    try:
        print(num/dem)
    except ZeroDivisionError:
        print('Denominator must not be zero')
        continue
    finally:
        print('goodbyee')


##Name Error Handling
try:
    print('My name is',name)
except NameError:
    
    name = input('enter name')
finally:
    print('My name is',name)
    print('goodbye')
