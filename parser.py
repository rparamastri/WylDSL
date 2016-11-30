from ply import lex

reserved = {
        'use'     : 'USE',
        'for'     : 'FOR',
        'instead' : 'INSTEAD'
        }

tokens = [
        'SYMBOL',
        'TEXT',
        'NODESTART',
        'ENDL',
        'SYMBOLCHARS',
        ] + list(reserved.values())

t_USE     = r'use'
t_FOR     = r'for'
t_INSTEAD = r'instead'

t_ignore_comment = r'\/\/[^\n]*'
t_ignore = ' \t'

def t_NODESTART(t): 
    r'>+'
    # count the number of >
    t.value = len(t.value)-1  # subtracts one so that the root is level 0
    return t

def t_SYMBOL(t):
    r'\$\w+'
    t.value = t.value[1:]  # removes the $ escape character
    return t

def t_TEXT(t):
    r'[\(\)\w]+'
    t.type = reserved.get(t.value, 'TEXT')
    return t

def t_ENDL(t):
    r';'
    t.value = '<BR/>'
    return t

def t_SYMBOLCHARS(t):
    r'[^\$>;\(\)(\/\/)\s]\S*'  # cannot define symbols starting with preceding tokens
    t.type = reserved.get(t.value, 'SYMBOLCHARS')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character {}".format(t.value[0]))
    t.lexer.skip(1)

lexer = lex.lex()

##############################   Yacc   ############################## 
from ply import yacc
from tree_structure import Node, Symbol

def p_program(p):
    '''program : user_symbols '''
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_user_symbols(p):
    '''user_symbols : user_symbol user_symbols
                    | nodes'''
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_user_symbol(p):
    '''user_symbol : USE SYMBOLCHARS FOR SYMBOL INSTEAD
                   | USE SYMBOLCHARS FOR SYMBOL'''
    if len(p) == 6:
        # trying to override a symbol that doesn't exist
        if p[4] not in Symbol.symbol_dict:
            print("Warning! Symbol ${} in line {} is not defined.\nOmit the "
                   "keyword 'instead' to define a new symbol".format(p[4])
                    )
        Symbol.symbol_dict[p[4]] = p[2]
    else:
        # defining a command that already exists
        if p[4] in Symbol.symbol_dict:
            print("Warning! Symbol ${} already exists as {}.\nAppend keyword"
                    " 'instead' to override an existing symbol".format(
                        p[4],
                        Symbol.symbol_dict[p[4]]
                        )
                    )
        Symbol.symbol_dict[p[4]] = p[2]
               
def p_nodes(p):
    '''nodes : node nodes
             | empty'''
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    else:
        p[0] = []

def p_empty(p):
    'empty :'
    pass

def p_node(p):
    'node : NODESTART content'
    p[0] = Node(p[1],         # depth within the tree
                p.lineno(1),  # line where node is defined
                p[2])

def p_content(p):
    '''content : term content
               | empty'''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = ""

def p_term(p):
    'term : ENDL'
    p[0] = p[1]

def p_term_symbol(p):
    'term : SYMBOL'
    try:
        p[0] = Symbol.symbol_dict[p[1]]
    except KeyError as err:
        print('The symbol keyword "{}" in line {} is not defined.\n'
              'Define symbol keywords by writing:\n'
              '\tkeyword $<keyword> for <symbol>\n'
              'where <symbol> is the literal string '
              'or HTML decimal values'.format(p[1], p.lineno(1))
             )
        raise 

def p_term_text(p):
    'term : TEXT'
    p[0] = '<I>' + p[1] + '</I>'  # italicize text

def p_error(p):
    raise SyntaxError(p)


parser = yacc.yacc()
    
