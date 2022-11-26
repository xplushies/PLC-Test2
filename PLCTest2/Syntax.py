from _typeshed import Self

class RDA:
    def __init__(self, tokens:list(str)) -> None:
        self.tokens = tokens
        self.current = 0
        self.currentToken = tokens[self.current]

    def stmt():
        '''
        <stmt> -->  <if_stmt> | <while_stmt> | <as_s> | <block> 
        '''
        pass

    def block(self):
        '''
        <block> -->  '{'  { <stmt> ';' }  '}'
        '''
        if self.currentToken == '{':
            self.getNextToken()
            self.stmt()
            self.getNextToken()
            if self.currentToken == ';':
                self.getNextToken()
                if self.currentToken == '}':
                    self.getNextToken()
                else:
                    self.error()
            else:
                self.error()
        else:
            self.error()

        pass

    def if_stmt():
        '''
        <if_stmt> --> 'if' '('  <bool_stmt>  ')' <stmt>  [ 'else'  <stmt> ]
        '''
        pass

    def while_stmt(self):
        '''
        <while_loop> --> 'while' '('  <bool_stmt>  ')' <stmt>
        '''
        if self.currentToken == 'while':
            self.getNextToken()
            if self.currentToken == '{':
                self.bool()
                self.getNextToken()
                if self.currentToken == '}':
                    self.getNextToken()
                    self.stmt()
                else:
                    self.error
            else:
                self.error()
        else:
            self.error()

    def as_t(self):
        '''
        <as_t> --> 'id' '=' <expr>
        '''
        if self.currentToken == 'id':
            self.getNextToken()
            if self.currentToken == '=':
                self.getNextToken()
                self.expr()
            else:
                self.error()
        else:
            self.error()
        pass

    def bool():
        '''
        <if_stmt> --> 'if' '('  <bool_stmt>  ')' <stmt>  [ 'else'  <stmt> ]
        '''
        pass

    def expr(self):
        '''
        <expr> --> <term> { ('+' | '-') <term> }
        '''
        self.term()
        while self.current == '+' or self.current == '-' :
            self.getNextToken()
            self.term()

    def term(self):
        '''
        <term> --> <factor> { ('*' | '\' | '%' ) <factor> }
        '''
        self.factor()
        while self.current == '*' or self.current == '\\' or self.current =='%':
            self.getNextToken()
            self.fector()

    def factor(self):
        '''
        <factor> --> 'id' | 'int_lit' | 'float_lit' | '(' ' <expr> ' ')'
        '''
        if self.currentToken == 'id' or self.currentToken == 'int_lit' or self.currentToken == 'float_lit':
            self.getNextToken()
        elif self.currentToken == '(':
            self.getNextToken() 
            self.expr()
            if self.currentToken == ')':
                self.getNextToken()
            else:
                self.error()
        else:
            self.error()

    def getNextToken(self):
        if self.current < len[self.tokens]:
            self.current += 1

        self.currentToken = self.tokens[self.current]

    def get():
        pass