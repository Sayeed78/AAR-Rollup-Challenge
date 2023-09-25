# Opens database (a csv file) and reads each row.

from header import *


database = 'F:\Sohail Sayeed\Repos\AAR-Rollup-Challenge\database'
subscriptions= '.\subscriptions.py'

'''
# Testing variables
sub_10 = '.\subscription_10.py'
sub_5 = '.\subscription_5.py'
'''


def file_reader(file):
    with open(database + file, 'r') as data:
        return csv.reader(data)

'''
    for row in reader:
        # skip labels row
        if line_count == 1:
            line_count += 1
            continue

        # strips unnecessary whitespace/characters
        end_date = (row[3].rstrip("]").strip(" ").rstrip(" '").strip("' "))
    return end_date
'''

'''
def create_subscription_list():
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
    return subscription_list



def file_reader():
    with open(database + subscriptions, 'r') as csvfile:
        reader = csv.reader(csvfile)
        line_count = 0
        with open(database + sub_10, 'a') as output:
            for row in reader:
                # Each row is a list of values from the CSV file
                print(row, file = output)
                line_count += 1

                if line_count >= 10:
                    break


def file_reader_str_striper(end_date):
    with open(database + sub_10, 'r') as gen_data:
    reader = csv.reader(gen_data)
    line_count = 1

    for row in reader:
        # skip labels row
        if line_count == 1:
            line_count += 1
            continue

        # strips unnecessary whitespace/characters
        end_date = (row[3].rstrip("]").strip(" ").rstrip(" '").strip("' "))
    return end_date

    
'''