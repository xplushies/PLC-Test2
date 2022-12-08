import re
#from _typeshed import Self
class Lex:
    lexList = []

    lexList.insert(0, "start")
    lexList.insert(1, "when")  #if statment
    lexList.insert(2, "con")  #while statement
    lexList.insert(3, "block")  #block statment
    lexList.insert(4, "as_")  #assignemt statement

    lexList.insert(5, "expr")  #expression
    lexList.insert(6, "term")  #term
    lexList.insert(7, "factor")  #factor

    lexList.insert(8, "bool_expr")  #boolean expression
    lexList.insert(9, "boolAnd")  #boolean and
    lexList.insert(10, "boolEqu")  #boolean equal to
    lexList.insert(11, "boolRel")  #boolean relation operation

    lexList.insert(12, "{")  #start
    lexList.insert(13, "}")  #end

    lexList.insert(14, "(")  #parenR bracket
    lexList.insert(15, ")")  #parenL bracket
    lexList.insert(16, "[")  #squareR bracket
    lexList.insert(17, "]")  #squareL bracket

    lexList.insert(18, "/")  #division
    lexList.insert(19, "%")  #modulous
    lexList.insert(20, "*")  #multiple
    lexList.insert(21, "+")  #addition
    lexList.insert(22, "-")  #subtraction

    lexList.insert(23, "=")  #assignment
    lexList.insert(24, "<")  #lessThan sign
    lexList.insert(25, ">")  #greaterThan sign
    lexList.insert(26, "<=") #greaterThanEqualTo
    lexList.insert(27, ">=") #greaterThanEqualTo
    lexList.insert(28, "==") #equalTo
    lexList.insert(29, "!=") #doesNotEqual

    lexList.insert(30, ":")   #colen
    lexList.insert(31, ";")   #semi colen
    lexList.insert(32, "@")   #1 byte memory suffix
    lexList.insert(33, "#")   #2 byte memory suffix
    lexList.insert(34, "$")   #3 byte memory suffix
    lexList.insert(35, "^")   #4 byte memory suffix
    lexList.insert(36, "&")   #and
    lexList.insert(37, "|")   #or
    lexList.insert(38, "\\")  #escape character
    lexList.insert(39, ",")   #comma
    lexList.insert(40, "else")#else

    lexList.insert(50, " ")  #space

class varName:
    varPattern = re.compile(r"\b\w{6,8}\b")
    pass

class num:
    numPattern = re.compile(r"(\d)+[@#$^]*")
    pass



