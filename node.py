
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

