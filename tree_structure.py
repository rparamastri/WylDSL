class Tree:
    def __init__(self, node_list):
        self.nodes = node_list
        self.edges = self.get_edges()

    def get_edges(self):
        """
        Given a list of Node objects, determine the tree's structure.
        Assumes that node_list is sorted by depth of nodes, then by line number.
        Returns a list of edges (x,y) where x and y are indices of nodes in
        node_list.
        """
        find_second_child = [None] * ( len(self.nodes)-2 )
        edges = []

        # Iterate through all the nodes but the last two.
        # The last two nodes could never have children.
        for i in range(len(self.nodes)-2):
            # if the next node is a child of this node
            if self.nodes[i].depth + 1 == self.nodes[i+1].depth:
                # store the depth of the second child
                find_second_child[i] = self.nodes[i].depth + 1

                edges.append((self.nodes[i].get_id(), self.nodes[i+1].get_id()))
            
            if self.nodes[i].depth in find_second_child:
                parent_index = find_second_child.index(self.nodes[i].depth)
                edge = (self.nodes[parent_index].get_id(), self.nodes[i].get_id())
                # this node is the second child of some other node
                if (edge not in edges) and (parent_index < i):
                    find_second_child[parent_index] = None
                    edges.append(edge)

        for i in range(len(self.nodes)-2,len(self.nodes)): 
            if self.nodes[i].depth in find_second_child:
                parent_index = find_second_child.index(self.nodes[i].depth)
                edge = (self.nodes[parent_index].get_id(), self.nodes[i].get_id())
                # this node is the second child of some other node
                if (edge not in edges) and (parent_index < i):
                    find_second_child[parent_index] = None
                    edges.append(edge)
        
        return edges

class Node:
    def __init__(self,depth,line,text):
        self.depth = depth
        self.line  = line
        self.text  = text

    def __repr__(self):
        return "Node({}, {}, {})".format(self.depth, self.line, self.text)

    def get_id(self):
        """Returns a unique id for the node based on depth and line number."""
        return "d{}l{}".format(self.depth, self.line)

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

    def __init__(self, keyword):
        self.keyword = keyword

    def get_symbol(self):
        try:
            return self.symbol_dict[self.keyword]
        except KeyError as e:  
            print('The symbol keyword "{}" is not defined.\n'
                  'Define symbol keywords by writing:\n'
                  '\tkeyword $<keyword> for <symbol>\n'
                  'where <symbol> is the literal string\n'
                  'or HTML decimal values'.format(self.keyword)
                 )
            raise

    def __repr__(self):
        return "Symbol({})".format(self.keyword)

