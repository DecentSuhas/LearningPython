import pandas as pd
df = pd.DataFrame()
print (df)

x = ['Python', 'Pandas']
df = pd.DataFrame(x)
print(df)

info = {'ID' :[101, 102, 103],'Department' :['B.Sc','B.Tech','M.Tech',]}
df = pd.DataFrame(info)
print (df)

info = {'one' : pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f']),
   'two' : pd.Series([1, 2, 3, 4, 5, 6, 7, 8], index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])}
d1 = pd.DataFrame(info)
print (d1)

d1['three'] = pd.Series([40,20,50],index=['a','b','c'])
print(d1)

d1['four'] = d1['one']+d1['three']
print(d1)

del d1['four']
print(d1)

del d1['three']
print(d1)

del d1['two']
print(d1)

d1.pop('one')
print(d1)

info = {'one': pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e']),
        'two': pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f'])}

df = pd.DataFrame(info)
print (df.loc['b'])

d = pd.DataFrame([[7, 8], [9, 10]], columns = ['x','y'])
d2 = pd.DataFrame([[11, 12], [13, 14]], columns = ['x','y'])
d = d.append(d2)
print(d)