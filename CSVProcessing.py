import pandas as pd

# These are the files we will be reading
data_sets = ['cars.csv', 'head.injury.csv']

for data in range(len(data_sets)):

    # Reads the CSV files with pandas
    DS1 = pd.read_csv(data_sets[data])

    print(data_sets[data])
    print('Columns', len(DS1.columns))
    print('Rows', len(DS1.values))
    print()

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

            # TODO mode may not work correctly, needs more testing on categorical data
            print('Column', i, 'mean is:', DS1_Sliced.mode())
            print()                                 # Blank line for formatting
        # Else the data is numerical
        else:
            print('Column', i, 'is numerical')
            numerical = True                        # There is numerical data, sets the Boolean to True
            DS1_Sliced = DS1.iloc[:, i:i + 1]       # Slices the data into a 1 wide column containing all of the rows
            print('Column', i, 'mean is:', DS1_Sliced.mean())
            print('Max value: ', DS1_Sliced.max())
            print('Min value: ', DS1_Sliced.min())
            print()                                 # Blank line for formatting

    # If statements to check if the values are numerical, categorical or both
    if categorical and not numerical:
        print("The data in", data_sets[data], "is categorical")
        print()
    if not categorical and numerical:
        print("The data in", data_sets[data], "is numerical")
        print()
    if categorical and numerical:
        print("The data in", data_sets[data], "both numerical and categorical")
        print()


