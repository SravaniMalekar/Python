import pandas as pd
import matplotlib.pyplot as plt
n=int(input('enter no. of students'))
list1=[]
for i in range(n):
    x= int(input('enter percent:'))
    list1.append(x)
plt.subplot(131)
plt.pie(list1)
plt.subplot(132)
plt.bar(list1,[1,2,3])
plt.subplot(133)
plt.stem(list1,[10,20,30])
plt.show()
