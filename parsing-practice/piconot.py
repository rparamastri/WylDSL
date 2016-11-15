import ply.lex as lex

tokens = [
        'STATE',
        'LBRACE',
        'RBRACE',
        'WALL',
        'BLANK',
        'ARROW',
        'COMMENT',
        'START_STATE',
        'DIRECTION' 
        ] 

t_START_STATE = r'[#]\s*start\s*='
t_ARROW       = r'->'
t_ignore      = ' \t'

literals = '{}_!'

def t_COMMENT(t):
    r'\/\/.*'
    pass

def t_DIRECTION(t):
    r'[NEWS]'  #TODO: allow lowercase news
    return t

def t_STATE(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    return t

def t_error(t):
    print("Illegal character {}".format(t.value[0]))
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

lexer = lex.lex()
