# tests active subscriptions

from datetime import *
import csv
from classes import *
from active_subscription import *

database = 'F:\Sohail Sayeed\Repos\AAR-Rollup-Challenge\database'
sub_10 = '.\subscription_10.py'
sub_5 = '.\subscription_5.py'

with open(database + sub_10, 'r') as gen_data:
    reader = csv.reader(gen_data)
    line_count = 1

    for row in reader:
        # skip labels row
        if line_count == 1:
            line_count += 1
            continue

        end_date = (row[3].rstrip("]").strip(" ").rstrip(" '").strip("' "))
        
        boolean = active_subscription(end_date)

        print(boolean)

        # Parse the date string into a date object
        #parsed_date = datetime.datetime.strptime(string, '%Y-%m-%d').date()

        #print(string)
        #print(parsed_date > datetime.date.today())

        #active_subscription(string)