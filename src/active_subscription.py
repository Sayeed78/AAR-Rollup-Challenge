# Contains method to check if there is an active subscription

from header import *

# Returns a boolean if the subscrition is active or not
def active_subscription(end_date):

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