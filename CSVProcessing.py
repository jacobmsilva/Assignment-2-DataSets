import pandas as pd

data_set_1 = 'cars.csv'
data_set_2 = 'head.injury.csv'

DS1 = pd.read_csv(data_set_1)
DS2 = pd.read_csv(data_set_2)

categorical = False
numerical = False

print("Data Set 1: ")
print('Columns', len(DS1.columns))
print('Rows', len(DS1.values))
print('First row of data: ', DS1.values[1])

for i in range(len(DS1.values[1])):
    if isinstance(DS1.values[1][i], str):
        print('Column', i, 'is categorical')
        categorical = True
    else:
        print('Column', i, 'is numerical')
        numerical = True


if categorical and not numerical:
    print("The data is categorical")
if not categorical and numerical:
    print("The data is numerical")
if categorical and numerical:
    print("The data is both numerical and categorical")

print(DS1.mean())
print(DS1.mode())

#for c in DS1.columns:
#    DS1[c].fillna()