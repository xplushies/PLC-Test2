import LexicalDict
import re
#import SyntaxAnalyzer

#lexList = LexicalDict.Lex.lexList

class LexAnalyzer:
    

#G1: at least 5 lexical errors

    file = open("partG1.txt")
    data = file.read()
    lex = data.split()

    numErrors = 0

    for token in lex:
        if token in LexicalDict.Lex.lexList:
            print(token + " is a lexeme.")
        elif LexicalDict.num.numPattern.fullmatch(token):
            print(token + " is a lexeme.")
        elif LexicalDict.varName.varPattern.fullmatch(token):
            print(token + " is a lexeme.")
        else:
            print(token + " is not a lexeme, so this is a lexical error.")
            numErrors += 1
    
    if numErrors == 1:
        print("There was " + str(numErrors) + " lexical error in the code.")
    else:
        print("There were " + str(numErrors) + " lexical errors in the code.")
    

#G2
    file = open("partG2.txt")
    data = file.read()
    lex = data.split()

    numErrors = 0

    for token in lex:
        if token in LexicalDict.Lex.lexList:
            print(token + " is a lexeme.")
        elif LexicalDict.num.numPattern.fullmatch(token):
            print(token + " is a lexeme.")
        elif LexicalDict.varName.varPattern.fullmatch(token):
            print(token + " is a lexeme.")
        else:
            print(token + " is not a lexeme, so this is a lexical error.")
            numErrors += 1
    
    if numErrors == 1:
        print("There was " + str(numErrors) + " lexical error in the code.")
    else:
        print("There were " + str(numErrors) + " lexical errors in the code.")


#G3
    file = open("partG3.txt")
    data = file.read()
    lex = data.split()

    numErrors = 0

    for token in lex:
        if token in LexicalDict.Lex.lexList:
            print(token + " is a lexeme.")
        elif LexicalDict.num.numPattern.fullmatch(token):
            print(token + " is a lexeme.")
        elif LexicalDict.varName.varPattern.fullmatch(token):
            print(token + " is a lexeme.")
        else:
            print(token + " is not a lexeme, so this is a lexical error.")
            numErrors += 1
    
    if numErrors == 1:
        print("There was " + str(numErrors) + " lexical error in the code.")
    else:
        print("There were " + str(numErrors) + " lexical errors in the code.")

    file = open("partG1.txt")
    data = file.read()
    lex = data.split()

    numErrors = 0

    for token in lex:
        if token in LexicalDict.Lex.lexList:
            print(token + " is a lexeme.")
        elif LexicalDict.num.numPattern.fullmatch(token):
            print(token + " is a lexeme.")
        elif LexicalDict.varName.varPattern.fullmatch(token):
            print(token + " is a lexeme.")
        else:
            print(token + " is not a lexeme, so this is a lexical error.")
            numErrors += 1
    
    if numErrors == 1:
        print("There was " + str(numErrors) + " lexical error in the code.")
    else:
        print("There were " + str(numErrors) + " lexical errors in the code.")


#G4
    file = open("partG4.txt")
    data = file.read()
    lex = data.split()

    numErrors = 0

    for token in lex:
        if token in LexicalDict.Lex.lexList:
            print(token + " is a lexeme.")
        elif LexicalDict.num.numPattern.fullmatch(token):
            print(token + " is a lexeme.")
        elif LexicalDict.varName.varPattern.fullmatch(token):
            print(token + " is a lexeme.")
        else:
            print(token + " is not a lexeme, so this is a lexical error.")
            numErrors += 1
    
    if numErrors == 1:
        print("There was " + str(numErrors) + " lexical error in the code.")
    else:
        print("There were " + str(numErrors) + " lexical errors in the code.")

    

