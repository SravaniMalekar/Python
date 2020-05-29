
#program1
class Myclass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self,name):
        print('hello miss'+self.name)
    
#calling the program1
me = Myclass('sravani',24)
print(me.name)

#program2
class T1:
    n=10
    def total(self,n):
        print(int(self.n)+int(n))
class T2:
    def total(self,s):
        print(len(str(s)))

#calling program2
t1=T1()
t2=T2()
t1.total(45)
t2.total(45)

#program3
class myclass:
    count=0
    def __init__(self):
        myclass.count +=1
    def __del__(self):
        myclass.count -=1
    @staticmethod
    def qty_object():
        return myclass.count

objs = [myclass() for i in range(10)]
print(myclass.qty_object())
import time as t
for i in range(len(objs)):
    try:
        print(myclass.qty_object())
        del objs[i]
        
    except:
        break
