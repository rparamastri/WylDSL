class Tree:
    def __init__(self, node_list):
        self.nodes = node_list

        # check for trailing linebreaks
        trails = [x for x,y in enumerate(self.nodes) if y.text[-5:] == '<BR/>']
        if len(trails) > 0:
            print("Warning! Linebreaks at the end of nodes may not be necessary.\n"
                    "Nodes at line(s) {} have trailing linebreaks.".format(
                        ', '.join(str(x) for x in trails)
                        )
                    )

        self.edges = []
        self.get_edges()

    def get_edges(self):
        """
        Given a list of Node objects, determine the tree's structure.
        Assumes that node_list is sorted by depth of nodes, then by line number.
        Returns a list of edges (x,y) where x and y are indices of nodes in
        node_list.
        """
        found_child = self.find_first_child()
        self.find_parent(found_child)

    def find_first_child(self):
        found_child = [i for i,node in enumerate(self.nodes[:-2]) 
                if node.depth+1 == self.nodes[i+1].depth
                ]
        for i in found_child:
            self.edges.append((self.nodes[ i ].get_id(), 
                               self.nodes[i+1].get_id()
                              ))

        return found_child

    def find_parent(self,found_child):
        for i in found_child:
            for node in self.nodes[i+2:]:
                if node.depth == self.nodes[i].depth + 1:
                    self.edges.append((self.nodes[i].get_id(), node.get_id()))
                    break
                elif node.depth == self.nodes[i].depth:
                    print("Error! Cannot construct tree.")
                    raise Exception

class Node:
    def __init__(self,depth,line,text):
        self.depth = depth
        self.line  = line
        self.text  = text

    def __repr__(self):
        return "Node({}, {}, {})".format(self.depth, self.line, self.text)

    def get_id(self):
        """Returns a unique id for the node based on depth and line number."""
        return "id{}".format(id(self))

class Symbol:
    symbol_dict = {
            'implies': '→',
            'iff': '↔',
            'not' : '¬',
            'and':'∧',
            'or' : '∨',
            'top': '⊤',
            'bottom':'⊥',
            'forall':'∀',
            'exists':'∃',
            'check':'✓'
            }

