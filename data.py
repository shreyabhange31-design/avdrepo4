import pandas as pd

data= {
    'name':['A','B','C'],
    'age':[30,20,20],
    'address':['Pune','Mumbai','CNS']
}

print('student Details')
df=pd.DataFrame(data)
print(df)