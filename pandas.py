import pandas as pd

#Writing Data to CSV using Pandas
df=pd.DataFrame([['jack',24],['rose',25],['sumit',24,'','male']],columns=['name','age','marks','gender'])
df.to_csv('person.csv')

#Reading data from web
##url="https://raw.githubusercontent.com/venky14/Machine-Learning-with-Iris-Dataset/master/Iris.csv"
url="https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"
columns=['length','width','variety']
df=pd.read_csv(url,delimiter=';',names=columns)

print(df.head())
