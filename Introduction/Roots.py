##from library from module
#import library
#import library as nickname
from cmath import *
a,b,c = int(input('enter a')),int(input('enter b')),int(input('enter c')) 
D = (b**2)-(4*a*c)
x= (-b + sqrt(D))/(2*a)
y= (-b - sqrt(D))/(2*a)
print(x,y)
