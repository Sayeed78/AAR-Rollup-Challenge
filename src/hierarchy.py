from classes.py import *

# File contains functions for datastructures relating to the hierarchy of the accounts.accounts

import csv

database = 'F:\Sohail Sayeed\Repos\AAR-Rollup-Challenge\database'
output_file = '.\subscription_10.py'

with open(database + '\subscriptions.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0
    with open(output_file, 'a') as output:
        for row in reader:
            # Each row is a list of values from the CSV file
            print(row, file = output)
            line_count += 1

            if line_count >= 10:
                break

