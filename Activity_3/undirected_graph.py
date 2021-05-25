import networkx as nx
import matplotlib.pyplot as plt

# Empty-like graph objects
u_graph = nx.Graph()

u_graph.add_node(1)
u_graph.add_node(2)
u_graph.add_node(3)
u_graph.add_node(4)
u_graph.add_node(5)
u_graph.add_node(6)
u_graph.add_edge(1,2)
u_graph.add_edge(2,4)
u_graph.add_edge(4,5)
u_graph.add_edge(4,3)
u_graph.add_edge(3,6)
u_graph.add_edge(3,1)
u_graph.add_edge(1,5)

nx.draw(u_graph, with_labels=True)
plt.savefig("undirected_graph.png")
