# Contains method to check if there is an active subscription

from header import *

# database and subscription file locations
database = 'F:\Sohail Sayeed\Repos\AAR-Rollup-Challenge\database'
subscriptions = '.\subscriptions.py'

# Testing variables/files
sub_10 = '.\subscription_10.py'
sub_5 = '.\subscription_5.py'

# Reads in the end_dates of subscriptions to determine if the subscription is active
def active_subscription():
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

            # returns true if subscription is active
            boolean = subscription_end_date(end_date)

            return boolean


# Helper function to convert string into a date
# Returns a boolean if the subscrition is active or not
def subscription_end_date(end_date):

    # Get the current date
    current_date = datetime.date.today()

    parsed_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()

    return (parsed_date > current_date)





########################################################################################################################
# Test version below
########################################################################################################################

'''
# Get the current date and time
current_datetime = datetime.datetime.now()

# Get the current date
current_date = current_datetime.date()

print("Current Date:", current_date)

date = datetime.date(2023, 9, 24)

print("Comparison:", date)

# if current_date is less than, then that means a future date
if (date >= current_date):
    print("active")
else:
    print("inactive")

'''