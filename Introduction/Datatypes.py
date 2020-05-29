>>> name =['nakul','sahil','rahul']
>>> marks=[40,50,60]
>>> dict(zip(name,marks))
{'nakul': 40, 'sahil': 50, 'rahul': 60}
>>> dict(name,marks)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    dict(name,marks)
TypeError: dict expected at most 1 argument, got 2
>>> marks.append(70)
>>> marks
[40, 50, 60, 70]
>>> marks.insert(3,80)
>>> marks
[40, 50, 60, 80, 70]
>>> met=[1,2,3]
>>> marks+met
[40, 50, 60, 80, 70, 1, 2, 3]
>>> 5*marks
[40, 50, 60, 80, 70, 40, 50, 60, 80, 70, 40, 50, 60, 80, 70, 40, 50, 60, 80, 70, 40, 50, 60, 80, 70]
>>> a = 'sumit'
>>> a*2
'sumitsumit'
>>> marks.index(50)
1
>>> met.clear()
>>> met
[]
>>> met = marks.copy()
>>> met.pop()
70
>>> met.pop(0)
40
>>> y= met.pop(1)
>>> y
60
>>> met.append(90)
>>> met.remove()
>>> met.remove(90)
>>> met
[50, 80]
>>> met = met+marks
>>> met.sort()
>>> met
[40, 50, 50, 60, 70, 80, 80]
>>> met.sort(reverse=True)
>>> met
[80, 80, 70, 60, 50, 50, 40]
>>> lst3=['a','c','z','e']
>>> lst3.sort
<built-in method sort of list object at 0x000001E13AC86540>
>>> lst3
['a', 'c', 'z', 'e']
>>> lst3.sort()
>>> lst3
['a', 'c', 'e', 'z']
>>> lst = met + lst3
>>> lst
[80, 80, 70, 60, 50, 50, 40, 'a', 'c', 'e', 'z']
>>> lst2=[1,2,50,3,80,50]
>>> lst2.reverse()
>>> lst2
[50, 80, 3, 50, 2, 1]
>>> lst2.count(50)
2
>>> lst1=[6,7,8]
>>> lst2=lst2+lst1
>>> lst2
[50, 80, 3, 50, 2, 1, 6, 7, 8]
>>> lst2.extend(lst1)
>>> lst2
[50, 80, 3, 50, 2, 1, 6, 7, 8, 6, 7, 8]
>>> if 100 in lst2:
	print(True)

	
>>> if 3 in lst2:
	print(True)

	
True
>>> 2 in lst2
True
>>> 100 in lst2
False
>>> 2 not in lst2
False
>>> x=3
>>> x
3
>>> x is not 3
False
>>> x == 3
True
>>> x != 5
True
>>> tup =(1,3,4)
>>> tup[2]
4
>>> tup[:2]
(1, 3)
>>> tup[1]
3
>>> tup
(1, 3, 4)
>>> lst2[:2]
[50, 80]
>>> tup1 =(1)
>>> tup1
1
>>> type(tup1)
<class 'int'>
>>> tup1 = (1,)
>>> tup1
(1,)
>>> tup2 =(2,3)
>>> tup1 = tup1 + tup2
>>> tup1
(1, 2, 3)
>>> dct={'name':'sravani','age':'20'}
>>> dct
{'name': 'sravani', 'age': '20'}
>>> dct.items()
dict_items([('name', 'sravani'), ('age', '20')])
>>> dct.keys()
dict_keys(['name', 'age'])
>>> dct.values()
dict_values(['sravani', '20'])
>>> students = {'name': ['a','b','c','d','e'], 'mail': []}
>>> students.keys()
dict_keys(['name', 'mail'])
>>> names=[]
>>> for values in students.values():
	print(values)

	
['a', 'b', 'c', 'd', 'e']
[]
>>> students['name']
['a', 'b', 'c', 'd', 'e']
>>> for name in students['name']:
	names.append(name)

	
>>> names
['a', 'b', 'c', 'd', 'e']
>>> std=[]
>>> std=students['name']
>>> std[4]
'e'
>>> for x,y in students.items():print(x,y)

name ['a', 'b', 'c', 'd', 'e']
mail []
>>> students['mail']='xyz@abc.in'
>>> students
{'name': ['a', 'b', 'c', 'd', 'e'], 'mail': 'xyz@abc.in'}
>>> set = {1,2,3,4,4}
>>> set
{1, 2, 3, 4}
>>> st={4,6,8,2,1,3}
>>> st
{1, 2, 3, 4, 6, 8}
>>> st.add(-5)
>>> st
{1, 2, 3, 4, 6, 8, -5}
>>> st2={6}
>>> st=st-st2
>>> st
{1, 2, 3, 4, 8, -5}
>>> st2.add(3)
>>> st2
{3, 6}
>>> st.union(st2)
{1, 2, 3, 4, 6, 8, -5}
>>> st.intersection(st2)
{3}
>>> st2.issubset(st)
False
>>> st.issubset(st2)
False
>>> st.isdisjoint(st2)
False
>>> st3={5}
>>> st.isdisjoint(st3)
True
