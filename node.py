
class Node:
    def __init__(self,depth,line,text):
        self.depth = depth
        self.line  = line
        self.text  = text

    def __repr__(self):
        return "Node({}, {}, {})".format(self.depth, self.line, self.text)

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
        except:  #TODO: write nicer error message
            print(e)

    def __repr__(self):
        return "Symbol({})".format(self.keyword)

