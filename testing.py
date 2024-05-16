import pickle
from graph import Graph
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(1000000)

g = Graph()
g.generate_nodes(0)
g.generate_graph(0)

# Open a file in write-binary mode
with open('data.pkl', 'wb') as file:
    # Serialize the object and write it to the file
    pickle.dump(g, file)
with open('data.pkl', 'rb') as file:
    # Deserialize the object from the file
    loaded_data = pickle.load(file)

# Print the loaded data
if g.get_as_dictionary() == loaded_data.get_as_dictionary():
    print("Amanda är en stockholmare")
else:
    print("Amanda är inte en stockholmare")