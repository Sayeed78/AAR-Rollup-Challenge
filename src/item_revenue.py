# Calculates the revenu for each subscription item
# The three data points are quantity, list_price, and discount from subscription_items.csv

import csv
import datetime

database = 'F:\Sohail Sayeed\Repos\AAR-Rollup-Challenge\database'
#data = '\subscription_items_5.csv'
data = '\subscription_items.csv'
output = 'revenue.csv'
file = database + data
outputfile = database + output

id =''
quantity = 0
list_price = 0
discount = 0
id_revenue = []
string = ''
labels = []
accounts = []
end_date = ''

with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        labels = next(reader)

        # Get the current date
        current_date = datetime.date.today()
        
        for row in reader: 
                #accounts.append(row)

                # strips unnecessary whitespace/characters
                end_date = (row[7].rstrip("]").strip(" ").strip("'").strip("'"))
                parsed_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()

                # if the subscription is active, calculate revenue
                id = row[0].strip(" ").strip("'").strip("[").strip("]").strip("'")
                if (parsed_date > current_date):
                        quantity = int(row[3].strip(" ").strip("'"))
                        list_price = int(row[4].strip(" ").strip("'"))
                        discount = float(row[5].strip(" ").strip("'").strip("]"))
                        revenue = quantity * list_price * discount
                        id_revenue.append([id, revenue])
                else:
                        id_revenue.append([id, 0])


for row in id_revenue:
    # parsing each column of a row
    for col in row:
        print("%10s"%col,end=" "),
    print('\n')