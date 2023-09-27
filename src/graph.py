# Creates edges between parent/child ids

import networkx as nx
import csv
import matplotlib.pyplot as plt

database = 'F:\Sohail Sayeed\Repos\AAR-Rollup-Challenge\database'
#data = '\subscription_items_5.csv'
#data = '\subscription_items.csv'
data = '/accounts.csv'
output = 'revenue.csv'
file = database + data
outputfile = database + output

ultimate_parents = []
id_edge_list = []
labels = []
id = ''
parent_id = ''


with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        #skip labels
        labels = next(reader)

        for row in reader:
            id = row[0].strip(" ").strip("'").strip("[").strip("]").strip("'")
            parent_id = row[1].strip(" ").strip("'").strip("[").strip("]").strip("'")
            # If has parent
            if (len(parent_id) > 0):
                id_edge_list.append((id, parent_id))
            else:
                    ultimate_parents.append(id)
                


# create the parent/child
heirarcy = nx.Graph()
heirarcy.add_edges_from(id_edge_list[:50])

print(list(nx.connected_components(heirarcy)))



#nx.draw_spring(heirarcy, with_labels=True)
#plt.show()


