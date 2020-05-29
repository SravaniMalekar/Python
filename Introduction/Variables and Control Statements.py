>>> a=1
>>> b=2
>>> c=3
>>> for i in range(3):
	print(a,b,c)

	
1 2 3
1 2 3
1 2 3
>>> for i in range(3):
	print(a,b,c,end='\n')

	
1 2 3
1 2 3
1 2 3
>>> for i in range(3):
	print(i,end='')

	
012
>>> for i in range(3):
	print(i,end=' ')

	
0 1 2 
>>> print(a,b,c,sep='     ')
1     2     3
>>> print(a,b,c,sep='\n')
1
2
3
>>> ord('a')
97
>>> chr(67)
'C'
>>> import numpy
>>> import seaborn
>>> chdir
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    chdir
NameError: name 'chdir' is not defined
>>> from math import sin
>>> sin(60)
-0.3048106211022167
>>> from math import *
>>> cos(60)
-0.9524129804151563
>>> import matplotlib.pyplot
>>> import matplotlib.pyplot as plt
>>> plt.plot()
[]
>>> plt.show()
>>> from math import *
>>> abs(-10)
10
>>> from cmath import *
>>> sqrt(-1)
1j
>>> a = int(input('enter value of a'))
enter value of a1
>>> b= int(input('enter value of b'))
enter value of b2
>>> c= int(input('enter value of c'))
enter value of c1
>>> x = (-b +- sqrt(b**2 - 4*a*c))/2*a
>>> x
(-1+0j)
>>> x
(-1+0j)
