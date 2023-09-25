# File contains Constructors for heirarchy of the accounts
# There is no child class. The idea is to create a heirarchy of accounts.

# Creates Ultimate Parent (or root parent)
class ultimate_parent:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.ultimate_parent(self)
        child.parent.append(self)

    # Method produces heiarchy of children when print() is called on object
    def __str__(self, level=0):
        ret = "\t" * level + self.account + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

# Creates Parent class
class parent:
    def __init__(self, account):
        self.account = account
        self.ultimate_parent = ultimate_parent
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.ultimate_parent = self.ultimate_parent
        child.parent.append(self)

    # Method produces heiarchy of children when print() is called on object
    def __str__(self, level=0):
        ret = "\t" * level + self.name + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

class account:
    def __int__(self, name):
        self.name = name
        self.account_type = account_type # Allows for different account types
        self.account_labels = [] # Stores labels of columns 
        self.account_data = [] # Stores data of columns
        
    # Helper function meant to be generated one row of a CSV file
    # In progress
    def add_account(self, data):
        self.account.append(data)



########################################################################################################################
# Below is version 2 of the classes object to potentially make the class simpler.
########################################################################################################################

class accountV2:
    def __int__(self, id, parent_id, name, ultimate_parent_id, arr, hierarchy_arr):
        self.name = name
        self.id = id
        self.parent_id = parent_id
        self.name = name
        self.ultimate_parent_id = ultimate_parent_id
        self.arr = arr
        self.hierarchy_arr = hierarchy_arr
        
########################################################################################################################
# Below are unused methods that can be used to expand this program, primarily to allow multiple parents.
########################################################################################################################


# below is an example if multiple parents are allowed.
'''
# Creates Parent class (has children)
class parent:
    def __init__(self, name, parent):
        self.name = name
        self.children = []
        self.parent = [parent] # List is used 

   
    # method only used if heirarchy allows mulitple parents
    def add_parent(self, parent):
        self.parent.append(parent)
   

    def add_child(self, child):
        self.children.append(child)

    def __str__(self, level=0):
        ret = "\t" * level + self.name + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
'''
