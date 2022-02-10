import pandas as pd
import numpy as np
#x = pd.Series()
#print(x)
print("creating series using array")

info = np.array(['P','a','n','d','a','s'])
a = pd.Series(info)
print(a)

print("creating series using dictionary")
info = {'x' : 0., 'y' : 1., 'z' : 2.}
a = pd.Series(info)
print(a)

print("creating series using scalar")
x = pd.Series(4,index = [0,1,2,3])
print(x)
x = pd.Series([1,2,3],index = ['a','b','c'])
print(x)
print(x[0])
print(x.index)
print(x.values)
a = pd.Series(data = [1,2,3])
b = pd.Series(data = [4.6,5.2,8.2])
index = ['x','y','z']
print(a.dtype)

print("map demo \n")

a = pd.Series(['Java','C','C++',np.nan])
print(a.map({'Java':'Core'}))

map2= a.map('i like {}'.format,na_action = 'ignore')
print(map2)