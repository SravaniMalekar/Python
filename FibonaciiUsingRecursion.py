a= int(input('enter n'))
def fibonacii(a):
    if a <=1:
        return a
    else:
        return (fibonacii(a-1)+fibonacii(a-2))

if a <=0:
    print('enter positive number')
else:
    for i in range(a):
        print(fibonacii(i))
