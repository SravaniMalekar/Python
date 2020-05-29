n=int(input('enter n'))
first =0
second =1
print(first)
print(second)
for i in range(2,n):
    
    ans = first + second
    print(ans)
    first = second
    second = ans
