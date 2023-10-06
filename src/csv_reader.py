import csv
import networkx as nx

# Dictionary to store parsed accounts
accounts_data = {}
# Directed Graph to build account hierarcy
hierachy = nx.DiGraph()
utimate_parents_list =()

# Parse accounts from CSV file
with open('accounts.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        account_id = row['id']
        parent_id = row['parent_id']
        name = row['name']
        ultimate_parent_id = row['ultimate_parent_id']
        arr = row['arr']
        hierarchy_arr = row['hierarchy_arr']

        # Parse arr as integer
        arr = int(arr)
        hierarchy_arr = int(hierarchy_arr)

        # Add account information to the dictionary
        accounts_data[account_id] = {
            'parent_id': parent_id,
            'name' : name,
            'ultimate_parent_id': ultimate_parent_id,
            'arr': arr
            'hierarchy_arr' : hierarchy_arr
        }
        
        # Adds direced edge from account to parent
        heirarcy.add_edges(account_id, parent_id)
        
with open('accounts.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        account_id = row['id']
        parent_id = row['parent_id']
        name = row['name']
        ultimate_parent_id = row['ultimate_parent_id']
        arr = row['arr']
        hierarchy_arr = row['hierarchy_arr']
 
    # Checks for 
    if hierarchy.has_node(row['ultimate_parent_id']) and any(pred for pred in G.predecessors(row['ultimate_parent_id'])):
        ultimate_parents_list.append(id)
    # Iterate until an ultimate parent is found
    else:
    

# Iterate through accounts to add ultimate_parent_id
for account_id, account_info in accounts_data.items():
    parent_id = account_info['parent_id']
    if parent_id is not None:
        # If parent_id exists, add ultimate_parent_id from parent account
        account_info['ultimate_parent_id'] = accounts_data[parent_id]['ultimate_parent_id']

# Print the updated accounts_data dictionary
print(accounts_data)
