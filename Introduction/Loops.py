>>> for i in range(2,5):
	for j in range(1,11):
		print('%d'%(i*j),end=' ')

		
2 4 6 8 10 12 14 16 18 20 3 6 9 12 15 18 21 24 27 30 4 8 12 16 20 24 28 32 36 40 
>>> for i in range(2,5):
	for j in range(1,11):
		print('%d'%(i*j),end=' ')
	print()

	
2 4 6 8 10 12 14 16 18 20 
3 6 9 12 15 18 21 24 27 30 
4 8 12 16 20 24 28 32 36 40 
>>> for i in range(1,11):
	for j in range(2,5):
		print('%d'%(i*j),end=' ')
	print()

	
2 3 4 
4 6 8 
6 9 12 
8 12 16 
10 15 20 
12 18 24 
14 21 28 
16 24 32 
18 27 36 
20 30 40 
>>> for i in range(1,11):
	for j in range(2,5):
		print('%d'%(i*j),end='\t')
	print()

	
2	3	4	
4	6	8	
6	9	12	
8	12	16	
10	15	20	
12	18	24	
14	21	28	
16	24	32	
18	27	36	
20	30	40
>>> i=2
>>> while(i<20):
	print(i)
	i+=1

	
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
>>> i=1
>>> j=2
>>> while i<=10:
	j=2
	while j<=6:
		print('%4d' %(i*j),end='\t')
		j+=1
	i+=1
	print()

	
   2	   3	   4	   5	   6	
   4	   6	   8	  10	  12	
   6	   9	  12	  15	  18	
   8	  12	  16	  20	  24	
  10	  15	  20	  25	  30	
  12	  18	  24	  30	  36	
  14	  21	  28	  35	  42	
  16	  24	  32	  40	  48	
  18	  27	  36	  45	  54	
  20	  30	  40	  50	  60
>>> for i in range(5):
	for j in range(i):
		print('*',end='\t')
	print('\n')

	


*	

*	*	

*	*	*	

*	*	*	*	