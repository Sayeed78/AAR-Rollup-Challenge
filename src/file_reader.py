# Opens database (a csv file) and reads each row.

from header import *


database = 'F:\Sohail Sayeed\Repos\AAR-Rollup-Challenge\database'
sub_10 = '.\subscription_10.py'
sub_5 = '.\subscription_5.py'


with open(database + '\subscriptions.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0
    with open(database + sub_10, 'a') as output:
        for row in reader:
            # Each row is a list of values from the CSV file
            print(row, file = output)
            line_count += 1

            if line_count >= 10:
                break

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
