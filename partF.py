from _typeshed import Self

class RecursiveAlgo:
    def __init__(self, tokens:list(str)) -> None:
        self.tokens = tokens
        self.current = 0
        self.currentToken = tokens[self.current]

    def Sen(self):

        #<stmt> -->  <if_stmt> | <while_stmt> | <as_s> | <block> 
        match self.currentToken:
            case 'when':
                self.when_Sen()
            case 'during':
                self.during_Sen()
            case 'id':
                self.as_Sen()
            case '{':
                self.block_Sen()
            case _:
                self.error()

    def block_Sen(self):

        #<block> -->  '{'  { <stmt> ';' }  '}'

        if self.currentToken == '{':
            self.getNextToken()
            while self.currentToken == 'when' or self.currentToken == 'during' or self.currentToken == 'id' or self.currentToken == '{':
                self.Sen()
                #self.getNextToken()
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

    #if_stmt
    def when_Sen(self):

        #<if_stmt> --> 'if' '('  <bool_stmt>  ')' <stmt>  [ 'else'  <stmt> ]

        match self.currentToken:
            case 'if':
                self.when_Sen()
            case 'during':
                self.during_Sen()
            case 'id':
                self.as_Sen()
            case '{':
                self.block_Sen()
            case _:
                self.error()

    #during_Sen
    def during_Sen(self):
        
        #<while_loop> --> 'while' '('  <bool_stmt>  ')' <stmt>

        if self.currentToken == 'during':
            self.getNextToken()
            if self.currentToken == '{':
                self.bool_Sen()
                self.getNextToken()
                if self.currentToken == '}':
                    self.getNextToken()
                    self.Sen()
                else:
                    self.error()
            else:
                self.error()
        else:
            self.error()

    def as_Sen(self):
        
        #<as_t> --> 'id' '=' <expr>
        
        if self.currentToken == 'iden':
            self.getNextToken()
            if self.currentToken == '=':
                self.getNextToken()
                self.expr()
            else:
                self.error()
        else:
            self.error()

    def bool_Sen(self):
        
        #<if_stmt> --> 'if' '('  <bool_stmt>  ')' <stmt>  [ 'else'  <stmt> ]
        if self.currentToken == 'when':
            self.getNextToken()
            if self.currentToken == '(':
                self.bool_Sen
                if self.currentToken == ')':
                    self.getNextToken()
                    self.Sen()
                    self.getNextToken()
                    if self.currentToken == 'else':
                        self.getNextToken()
                        self.Sen()
                    else:
                        self.error()
                else:
                    self.error()
            else:
                self.error()
        else:
            self.error()

    def expr(self):
        '''
        #<expr> --> <term> { ('+' | '-') <term> }
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
            self.factor()

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

    def error(self):
        print("An error has occured due to a syntactical error in the code.")