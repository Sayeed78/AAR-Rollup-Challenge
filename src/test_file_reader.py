# Creating a file_reader function can eliminte repeated code.
# Currently every method opens a new instance of a file.
# This function opens database (a csv file) and reads each row. 
# Unfinished.

import csv

database = 'F:\Sohail Sayeed\Repos\AAR-Rollup-Challenge\database'
subscriptions = '.\subscriptions.csv'
sub_items = '.\subscription_items.csv'

file = '.\subscription_items.csv'
ids = '.\ids.csv'

labels = []
rows = []

# Testing variables
sub_10 = '.\subscription_10.csv'
sub_5 = '.\subscription_5.csv'

#def file_cleaner(file):
with open(database + file, 'r') as data:
        reader = csv.reader(data)
        col_length = 0
        labels = next(reader)
        for row in reader: 
                rows.append(row)
        print("Total no. of rows: %d"%(reader.line_num))

 
# printing the field names
print('Label names are:' + ', '.join(label for label in labels))

print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    # parsing each column of a row
    for col in row:
        print("%10s"%col,end=" "),
    print('\n')



'''
        with open(database + ids, 'a') as output:
            for row[:5] in reader: 
                rows.append(row)
                #print(row, file = output)
'''
        