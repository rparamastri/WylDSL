
from tree_structure import Tree
from graphviz import Graph

def draw(tree, f_format, fname, clean):
    g = Graph(format=f_format, node_attr={'shape':'plaintext'})

    for tree_node in tree.nodes:
        g.node(tree_node.get_id(), '<'+tree_node.text+'>')

    for tree_edge in tree.edges:
        g.edge(*tree_edge)

    g.render(fname, cleanup=clean)

