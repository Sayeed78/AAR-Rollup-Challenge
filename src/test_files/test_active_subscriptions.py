# tests active subscriptions

from header import *

database = 'F:\Sohail Sayeed\Repos\AAR-Rollup-Challenge\database'
subscriptions = '.\subscriptions.py'

# Testing variables
sub_10 = '.\subscription_10.py'
sub_5 = '.\subscription_5.py'

i = 0
while i < 10:
    if (active_subscription()):
          print('true')
    else:
         print('false')
    i += 1


'''
with open(database + sub_10, 'r') as data:
    reader = csv.reader(data)
    line_count = 1

    for row in reader:
        # skip labels row
        if line_count == 1:
            line_count += 1
            continue

        # strips unnecessary whitespace/characters
        end_date = (row[3].rstrip("]").strip(" ").rstrip(" '").strip("' "))

        boolean = active_subscription(end_date)

        print(boolean)
        '''