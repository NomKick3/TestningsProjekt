import pickle
from Graph import Graph
import matplotlib.pyplot as plt

g = Graph()
g.generate_nodes(10)
g.generate_graph(10)

# Open a file in write-binary mode
with open('data.pkl', 'wb') as file:
    # Serialize the object and write it to the file
    pickle.dump(g, file)

with open('data.pkl', 'rb') as file:
    # Deserialize the object from the file
    loaded_data = pickle.load(file)

# Print the loaded data
g.plot_graph()
loaded_data.plot_graph()
plt.show()
