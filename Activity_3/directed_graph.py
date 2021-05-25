import networkx as nx
import matplotlib.pyplot as plt

# Empty-like graph objects
d_graph = nx.DiGraph()

d_graph.add_node(1)
d_graph.add_node(2)
d_graph.add_node(3)
d_graph.add_node(4)
d_graph.add_node(5)
d_graph.add_node(6)
d_graph.add_edge(1,2)
d_graph.add_edge(3,4)
d_graph.add_edge(5,6)
d_graph.add_edge(6,1)
d_graph.add_edge(3,1)
d_graph.add_edge(4,2)
d_graph.add_edge(1,5)

nx.draw(d_graph, with_labels=True)
plt.savefig("directed_graph.png")
