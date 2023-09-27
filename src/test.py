# File used for testing purposes

import csv


database = 'F:\Sohail Sayeed\Repos\AAR-Rollup-Challenge\database'
sub = '\subscriptions.csv'
sub_items = '\subscription_items.csv'
sub_10 = '.\subscription_10.csv'
sub_5 = '.\subscription_5.csv'
sub_items_10 = '.\subscription_items_5.csv'


with open(database + sub_items, 'r') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0
    with open(database + sub_items_10, 'w') as output:
        for row in reader:
            # Each row is a list of values from the CSV file
            print(row, file = output)
            line_count += 1

            if line_count >= 10:
                break

'''
subscription_list = []
labels = []

with open(database + sub_10, 'r') as gen_data:
    reader = csv.reader(gen_data)
    line_count = 0
    with open(database + sub_5, 'a') as output:
        for row in reader:
            # Each row is a list of values from the CSV file
            
            if line_count == 0:
                print(row, labels)
                line_count += 1
            elif line_count >= 10:
                break
            else:
                subscription_list.append(parent(row))

#print(subscription_list.account)

'''

