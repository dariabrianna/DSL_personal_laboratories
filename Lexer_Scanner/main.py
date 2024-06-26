import re

# Token types
IDENTIFIER = 'IDENTIFIER'
INTEGER = 'INTEGER'
CHAR = 'CHAR'
STRING = 'STRING'
PLUS = 'PLUS'
MINUS = 'MINUS'
MULTIPLY = 'MULTIPLY'
DIVIDE = 'DIVIDE'
ASSIGN = 'ASSIGN'
LPAREN = 'LPAREN'
RPAREN = 'RPAREN'
EQUAL = 'EQUAL'
LESS = 'LESS'
GREATER = 'GREATER'
LESS_EQUAL = 'LESS_EQUAL'
GREATER_EQUAL = 'GREATER_EQUAL'
FOR = 'FOR'
IN = 'IN'
RANGE = 'RANGE'
IF = 'IF'
ELSE = 'ELSE'
PRINT= 'PRINT'
COLON = 'COLON'
INCREMENT = 'INCREMENT'
SPACE = 'SPACE'
NEWLINE = 'NEWLINE'
EOF = 'EOF'

# Regular expressions for token patterns
TOKEN_REGEX = [
    (r'[a-zA-Z][a-zA-Z0-9_]*', IDENTIFIER),
    (r'\d+', INTEGER),
    (r'\'[a-zA-Z\s][a-zA-Z\s]+\'', STRING),
    (r'\'[a-zA-Z]\'', CHAR),
    (r'\+=', INCREMENT),
    (r'\+', PLUS),
    (r'-', MINUS),
    (r'\*', MULTIPLY),
    (r'/', DIVIDE),
    (r'\(', LPAREN),
    (r'\)', RPAREN),
    (r'==', EQUAL),
    (r'<=', LESS_EQUAL),
    (r'>=', GREATER_EQUAL),
    (r'<', LESS),
    (r'>', GREATER),
    (r'=', ASSIGN),
    (r':', COLON),
    (r'\s+', SPACE),
    (r'\n', NEWLINE)
]

KEY_WORDS = ['for', 'in', 'range', 'if', 'else', 'print', 'while' ]

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f'Token({self.type}, {self.value})'


class Lexer:
    def __init__(self, text):
        self.text = text.strip()  
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None  # Current character in examination

    def advance(self):
        """verificam urmatorul caracter in input"""
        self.pos += 1
        if self.pos >= len(self.text):
            self.current_char = None  # indica finalul inputului
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace_and_newlines(self):
        """face skip la spatii si new line caractere"""
        while self.current_char is not None and self.current_char in [' ', '\n']:
            self.advance()

    def error(self):
        raise Exception('Invalid character')

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char in [' ', '\n']:
                self.skip_whitespace_and_newlines()
                continue

            for pattern, token_type in TOKEN_REGEX:
                regex = re.compile(pattern)
                match = regex.match(self.text, self.pos)
                if match:
                    value = match.group(0)
                    # avanseaza daca face match la token 
                    for _ in range(len(value)):
                        self.advance()
                    if value in KEY_WORDS:
                        return Token(value.upper(), value)
                    else:
                        return Token(token_type, value)

            self.error()  # daca nu gasim niciun match ridicam eroare

        return Token(EOF, None)  # Return an EOF token at the end of the input



if __name__ == '__main__':
    lexer = Lexer("weight <= 34\n if weight >= 35: print('You are a child')\n else: print('You are a big child')\n")
    while True:
        token = lexer.get_next_token()
        if token.type == EOF:
            break
        print(token)