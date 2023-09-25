# Calculates the revenu for each subscription item
# The three data points are quantity, list_price, and discount from subscription_items.csv

from header import *

database = 'F:\Sohail Sayeed\Repos\AAR-Rollup-Challenge\database'
data = '\subscription_items_5.py'
file = database + data

id =''
quantity = 0
list_price = 0
discount = 0
revenue = 0
string = ''
with open(database + data, 'r') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
         # skip labels row
        if line_count == 0:
            line_count += 1
            continue

        string = row[4].lstrip("[").rstrip("]").rstrip(" ").lstrip(" ").strip('"')
        print(string)
        quantity = int(string)

        if line_count == 5:

'''
        print(
        row[0].lstrip("[").rstrip("]").rstrip(" ").lstrip(" ").strip('"'), 
        row[1].lstrip("[").rstrip("]").strip(" ").lstrip(" ").strip('"'), 
        row[2].lstrip("[").rstrip("]").strip(" ").lstrip(" ").strip('"'), 
        row[3].lstrip("[").rstrip("]").strip(" ").lstrip(" ").strip('"'), 
        row[4].lstrip("[").rstrip("]").strip(" ").lstrip(" ").strip('"'), 
        row[5].lstrip("[").rstrip("]").strip(" ").lstrip(" ").strip('"'), 
        row[6].lstrip("[").rstrip("]").strip(" ").lstrip(" ").strip('"'),
        row[7].lstrip("[").rstrip("]").strip(" ").lstrip(" ").strip('"'),
        )
'''




        #quantity = int(row[3])
        #list_price = int(row[4])
        #discount = int(row[5])

        #string = (row[3].rstrip("]").strip(" ").lstrip(" "))
        #list_price = (row[4].rstrip("]").strip(" "))
        #discount = (row[5].rstrip("]").strip(" "))

        #quantity = float(string)


        #print(row[0], row[3], row[4], row[5])

        #print(quantity, list_price, discount)

        #revenue = quantity * list_price * discount

        #print(string)


