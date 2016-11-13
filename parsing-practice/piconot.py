import ply.lex as lex

reserved = {
        r'[N|E|W|S]'  : 'DIRECTION'
        }

tokens = [
        'STATE',
        'LBRACE',
        'RBRACE',
        'WALL',
        'BLANK',
        'ARROW',
        'COMMENT',
        'START_STATE'
        ] + list(reserved.values()) 

t_START_STATE = r'\#start ='
t_LBRACE      = r'\{'
t_RBRACE      = r'\}'
t_WALL        = r'\!'
t_BLANK       = r'_'
t_ARROW       = r'->'
t_ignore      = ' \t'

def t_STATE(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'STATE')
    return t

def t_COMMENT(t):
    r'//*'
    pass

def t_error(t):
    print("Illegal character {}".format(t.value[0]))
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

lexer = lex.lex()

