import matplotlib.pyplot as plt
import networkx as nx

# create a new directed graph
G = nx.DiGraph()

# set the nodes
G.add_nodes_from(['q0', 'q1', 'q2', 'q3'])

# set the initial state
G.add_node('', style='invisible')
G.add_edge('', 'q0')

# set the transitions
G.add_edge('q0', 'q0', label='a')
G.add_edge('q0', 'q1', label='a')
G.add_edge('q1', 'q2', label='b')
G.add_edge('q2', 'q2', label='a')
G.add_edge('q2', 'q3', label='c')
G.add_edge('q3', 'q3', label='c')

# set the final states
G.add_node('q3', shape='doublecircle')

# get the positions of the nodes using the spring layout algorithm
pos = nx.spring_layout(G)

# set the labels
labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
nx.draw_networkx_labels(G, pos)

# set the colors and styles of the nodes and edges
node_colors = ['white' if node != 'q3' else 'lightgray' for node in G.nodes()]
edge_styles = ['solid' if label != 'λ' else 'dashed' for (u, v, label) in G.edges(data='label')]
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_shape='s', node_size=300)
nx.draw_networkx_edges(G, pos, edge_color='black', style=edge_styles)

# show the graph
plt.axis('off')
plt.show()
