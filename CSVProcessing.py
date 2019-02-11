import pandas as pd

# These are the files we will be reading
# TODO: scan directory for CSV files and use those by default
data_set_1 = 'cars.csv'
data_set_2 = 'head.injury.csv'

# Reads the CSV files with pandas
DS1 = pd.read_csv(data_set_1)
DS2 = pd.read_csv(data_set_2)

print("Data Set 1: ")
print('Columns', len(DS1.columns))
print('Rows', len(DS1.values))
print('First row of data: ', DS1.values[1])

# Booleans used in determining what types of data are in the columns
categorical = False
numerical = False

# Loops through the first row to determine what kind of data we are looking at
for i in range(len(DS1.values[1])):
    # If the data is categorical
    if isinstance(DS1.values[1][i], str):
        print('Column', i, 'is categorical')
        categorical = True                      # There is categorical data, sets Boolean to True
        DS1_Sliced = DS1.iloc[:, i:i + 1]       # Slices the data into a 1 wide column containing all of the rows
        print('Column', i, 'mean is:', DS1_Sliced.mode())
    # Else the data is numerical
    else:
        print('Column', i, 'is numerical')
        numerical = True                        # There is numerical data, sets the Boolean to True
        DS1_Sliced = DS1.iloc[:, i:i + 1]       # Slices the data into a 1 wide column containing all of the rows
        print('Column', i, 'mean is:', DS1_Sliced.mean())

# If statements to check if the values are numerical, categorical or both
if categorical and not numerical:
    print("The data is categorical")
if not categorical and numerical:
    print("The data is numerical")
if categorical and numerical:
    print("The data is both numerical and categorical")


