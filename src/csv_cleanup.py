# This files cleans up the csv file

import csv

database = 'F:\Sohail Sayeed\Repos\AAR-Rollup-Challenge\database'
output_file = '.\subscription_10.py'

labels = []
cleaned_file = '.\clean_sub_10.py'

with open(database + '\subscriptions.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0
    with open(output_file, 'a') as output:
        for row in reader:
            # skip header line
            if line_count == 0:
                line_count +=1
                continue

            
            print(row)



            # get only first 10 elements
            if line_count >= 10:
                break