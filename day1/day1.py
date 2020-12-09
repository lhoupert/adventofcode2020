import pandas as pd

data=pd.read_csv('day1_input.csv',name='X')

listoftwo = [ x for y in data['X']  for x in  data['X']  if x + y ==2020]
print(listoftwo[0] *listoftwo[1])

listexpenses = [ x for z in data['X'] for y in data['X']  for x in  data['X']  if x + y + z ==2020]
# use the set() property to get only the unique element from listexpenses
listofthree = list(set(listofthree))
[print(x) for x in listofthree]
print('\n'.join([str(x) for x in listofthree]))
print(listofthree[0] * listofthree[1] * listofthree[2])
