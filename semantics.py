
from tree_structure import Tree
from graphviz import Graph

def draw(tree, f_format, fname, dot_file):
    g = Graph(format=f_format, node_attr={'shape':'plaintext'})

    # add nodes to the graph
    for tree_node in tree.nodes:
        g.node(tree_node.get_id(), '<'+tree_node.text+'>')

    # add edges to the graph
    for tree_edge in tree.edges:
        g.edge(*tree_edge)

    g.render(fname, cleanup = not dot_file)

