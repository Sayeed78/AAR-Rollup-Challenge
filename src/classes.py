# File contains methods used in this project







# Constructors for heirarchy

# Creates Ultimate Parent (or root parent)
class ultimate_parent:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.ultimate_parent(self)
        child.parent.append(self)


    def __str__(self, level=0):
        ret = "\t" * level + self.account + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

# Creates Parent class (has children)
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

    def __str__(self, level=0):
        ret = "\t" * level + self.name + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

class account:
    def __int__(self, name, account_type):
        self.name = name
        self.account_type = account_type # Allows for different account types
        self.account_labels = [] # Stores lable of columns 
        self.account_data = [] # Stores data of columns
        
    # Helper function meant to be generated one row of a CSV file
    def add_account(self, data):
        self.account.append(data)



# Methods for extracting data









# Unneccassy class
'''
# Creates Child class (bottom of heirarchy with no children)
class child:
    def __init__(self, name):
        self.name = name
        self.parent = parent 

    def __str__(self, level=0):
        ret = "\t" * level + self.name + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
'''















########################################################################################################################
# Below are unused methods that can be used to expand this program, such as allowing multiple parents.
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