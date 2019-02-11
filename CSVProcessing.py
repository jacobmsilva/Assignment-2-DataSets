import pandas as pd
import matplotlib as plt
import numpy as np

# TODO: Test categorical data, specifically the mode
# TODO: add test for useless data, Timestamps
# TODO: histograms per each column: numerical data
# TODO: bar plot for categorical columns


# These are the files we will be reading
data_sets = ['cars.csv', 'head.injury.csv']

# Loops through each csv file in 'data_sets'
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
        is_useless = False                          # Boolean to determine if a column contains useless information

        # If the data is categorical
        if isinstance(DS1.values[1][i], str):
            print('Column', i, 'is categorical')
            categorical = True                      # There is categorical data, sets Boolean to True
            DS1_Sliced = DS1.iloc[:, i:i + 1]       # Slices the data into a 1 wide column containing all of the rows

            # TODO mode may not work correctly, needs more testing on categorical data
            print('Column', i, 'mean is:', DS1_Sliced.mode())

            # TODO: Add barplot here
            print()                                 # Blank line for formatting

        # Else the data is numerical
        else:
            DS1_Sliced = DS1.iloc[:, i:i + 1]  # Slices the data into a 1 wide column containing all of the rows

            # Loops through each element in the column:
            #   Checks to see if the column is just the index for the row
            for index, row in DS1_Sliced.iterrows():
                if row[0] == index+1:
                    is_useless = True
                else:
                    is_useless = False

            # If the column is not indexes, carry on with processing the data
            if not is_useless:
                print('Column', i, 'is numerical')
                numerical = True                        # There is numerical data, sets the Boolean to True
                print('Column', i, 'mean is:', DS1_Sliced.mean())
                print('Max value: ', DS1_Sliced.max())
                print('Min value: ', DS1_Sliced.min())

                # TODO: add histogram here

                print()                                 # Blank line for formatting
            # Else the column is indexes
            else:
                print('Column', i,  'are indexes of rows, and therefore useless')
                print()

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

