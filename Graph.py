import random
import networkx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self) -> None:
        self.nodes = []
        self.G = networkx.DiGraph()
    
    def generate_nodes(self, n = 100) -> None:
        for i in range(n):
            self.nodes.append(Node(i))

    def generate_graph(self, n = 100) -> None:
        for _ in range(n):
            rnd1 = random.randint(0,len(self.nodes)-1)
            rnd2 = random.randint(0,len(self.nodes)-1)
            
            self.nodes[rnd1].add_child(self.nodes[rnd2])

    def plot_graph(self) -> None:
        for node in self.nodes:
            self.G.add_edges_from(node.get_vertices())

        pos = networkx.spring_layout(self.G)
        networkx.draw_networkx_nodes(self.G,pos,cmap=plt.get_cmap("jet"),node_size=500)
        networkx.draw_networkx_labels(self.G,pos)
        networkx.draw_networkx_edges(self.G,pos)

    def get_as_dictionary(self):
        n_dict = {}
        for node in self.nodes:
            children = []
            for child in node.children:
                children.append(child.name)
            n_dict[node.name] = children
        return n_dict

class Node:
    def __init__(self,index) -> None:
        self.name = index
        self.children = []
        self.parents = []

    def add_child(self, _child) -> None:
        self.children.append(_child)
        _child.add_parent(self)

    def add_parent(self, _parent) -> None:
        self.parents.append(_parent)

    def get_vertices(self) -> list:
        vertices = []
        for i in self.children:
            vertices.append((self.name,i.name))
        return vertices

if __name__ == "__main__":
    graph = Graph()

    graph.generate_nodes()
    graph.generate_graph()
    graph.plot_graph()