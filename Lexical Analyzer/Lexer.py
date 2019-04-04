import re
import time

# Author   AHMAD AFRAZ KHAN
# Reg # :  2015-CS-27


# All Tokens     implemented
# KEYWORDS:      if, do, not, else, end, program,
#                function ,while ,then, var,
#                procedure, of, begin, array, integer
# IDENTIFIERS
# REL OPERATORS: =, >, <, >=, <=, <>, 
# NUMBERS:       fraction, exponents
# COMMENTS
# WHITE SPACES,  BLANKS, NEWLINE 


# to check numbers
ints = ['0','1','2','3','4','5','6','7','8','9']

# class object for lexer analyzer
class lexer(object):

    def __init__(self,source_code):

        # Create a word list of the source word
        self.source_code = source_code
        # this will track the index of the word list in source code
        self.source_index = 0

    # this function generates tokens from input stream
    def tokenize(self):


        # all tokens created by lexer will be stored here
        tokens = []

        # this is the first token from source code
        word =  self.source_code[0]
        
        # loop through each  word in source code to generate tokens 
        while (1):
            time.sleep(2)
            
            # this checks for end of file
            if( word=="end" ):
                break
            

            # this checks for comments in source code
            if (word == "{"):
                word = self.getNextToken()
                # this chacks for any nested comments sections
                while(word != "}"):
                    word = self.getNextToken()
                
                word = self.getNextToken()

            # this checks for whitespaces & newlines
            elif word == " " or word == "\n":
                word = self.getNextToken()
            
            # check for if keyword
            elif word == 'i':
                identifier = word
                word = self.getNextToken()
                if word == 'f':
                    identifier += word
                    word = self.getNextToken()
                    if word == ' ' or word == ':':
                        tokens.append(['KEYWORD','if'])
                        word = self.getNextToken()
                    else:
                        while word and (word!= ' '):
                            identifier += word
                            word = self.getNextToken()
                        tokens.append(['IDENTIFIER',identifier])
                        identifier = ""    
                else:
                    while word and (word!= ' '):
                        identifier += word
                        word = self.getNextToken()
                    tokens.append(['IDENTIFIER',identifier])
                    identifier = ""
                

            # check for do keyword
            elif word == 'd':
                identifier = word
                index = self.source_index
                word = self.getNextToken()
                if word == 'o':
                    identifier += word
                    word = self.getNextToken()
                    if word == ' ':
                        tokens.append(['KEYWORD','do'])
                        word = self.getNextToken()
                    else:
                        while word and (word!= ' '):
                            identifier += word
                            word = self.getNextToken()
                        tokens.append(['IDENTIFIER',identifier])
                        identifier = ""    
                else:
                    while word and (word!= ' '):
                        identifier += word
                        word = self.getNextToken()
                    tokens.append(['IDENTIFIER',identifier])
                    identifier = ""
            
            # check for of keyword
            elif word == 'o':
                identifier = word
                word = self.getNextToken()
                if word == 'f':
                    identifier += word
                    word = self.getNextToken()
                    if word == ' ':
                        tokens.append(['KEYWORD','of'])
                        word = self.getNextToken()
                    else:
                        while word and (word!= ' '):
                            identifier += word
                            word = self.getNextToken()
                        tokens.append(['IDENTIFIER',identifier])
                        identifier = ""
                else:
                    while word and (word!= ' '):
                        identifier += word
                        word = self.getNextToken()
                    tokens.append(['IDENTIFIER',identifier])
                    identifier = ""

            # check for not keyword
            elif word == 'n':
                identifier = word
                word = self.getNextToken()
                if word == 'o':
                    identifier += word
                    word = self.getNextToken()
                    if word == 't':
                        identifier += word
                        word = self.getNextToken()
                        if word == ' ':
                            tokens.append(['KEYWORD','not'])
                            word = self.getNextToken()
                        else:
                            while word and (word!= ' '):
                                identifier += word
                                word = self.getNextToken()
                            tokens.append(['IDENTIFIER',identifier])
                            identifier = ""
                    else:
                        while word and (word!= ' '):
                            identifier += word
                            word = self.getNextToken()
                        tokens.append(['IDENTIFIER',identifier])
                        identifier = ""
                else:
                    while word and (word!= ' '):
                        identifier += word
                        word = self.getNextToken()
                    tokens.append(['IDENTIFIER',identifier])
                    identifier = ""
            
            # check for var keyword
            elif word == 'v':
                identifier = word
                word = self.getNextToken()
                if word == 'a':
                    identifier += word
                    word = self.getNextToken()
                    if word == 'r':
                        identifier += word
                        word = self.getNextToken()
                        if word == ' ':
                            tokens.append(['KEYWORD','var'])
                            word = self.getNextToken()
                        else:
                            while word and (word!= ' '):
                                identifier += word
                                word = self.getNextToken()
                            tokens.append(['IDENTIFIER',identifier])
                            identifier = ""
                    else:
                        while word and (word!= ' '):
                            identifier += word
                            word = self.getNextToken()
                        tokens.append(['IDENTIFIER',identifier])
                        identifier = ""
                else:
                    while word and (word!= ' '):
                        identifier += word
                        word = self.getNextToken()
                    tokens.append(['IDENTIFIER',identifier])
                    identifier = ""
            
            # check for then keyword
            elif word == 't':
                identifier = word
                word = self.getNextToken()
                if word == 'h':
                    identifier += word
                    word = self.getNextToken()
                    if word == 'e':
                        identifier += word
                        word = self.getNextToken()
                        if word == 'n':
                            identifier += word
                            word = self.getNextToken()
                            if word == ' ' :
                                tokens.append(['KEYWORD','then'])
                                word = self.getNextToken()
                            else:
                                while word and (word!= ' '):
                                    identifier += word
                                    word = self.getNextToken()
                                tokens.append(['IDENTIFIER',identifier])
                                identifier = ""
                        else:
                            while word and (word!= ' '):
                                identifier += word
                                word = self.getNextToken()
                            tokens.append(['IDENTIFIER',identifier])
                            identifier = ""
                    else:
                        while word and (word!= ' '):
                            identifier += word
                            word = self.getNextToken()
                        tokens.append(['IDENTIFIER',identifier])
                        identifier = ""
                else:
                    while word and (word!= ' '):
                        identifier += word
                        word = self.getNextToken()
                    tokens.append(['IDENTIFIER',identifier])
                    identifier = ""
            
            # check for else keyword
            elif word == 'e':
                identifier += word
                word = self.getNextToken()
                if word == 'l':
                    identifier += word
                    word = self.getNextToken()
                    if word == 's':
                        identifier += word
                        word = self.getNextToken()
                        if word == 'e':
                            identifier += word
                            word = self.getNextToken()
                            if word == ' ' :
                                tokens.append(['KEYWORD','else'])
                                word = self.getNextToken()
                            else:
                                while word and (word!= ' '):
                                    identifier += word
                                    word = self.getNextToken()
                                tokens.append(['IDENTIFIER',identifier])
                                identifier = ""
                        else:
                            while word and (word!= ' '):
                                identifier += word
                                word = self.getNextToken()
                            tokens.append(['IDENTIFIER',identifier])
                            identifier = ""
                    else:
                        while word and (word!= ' '):
                            identifier += word
                            word = self.getNextToken()
                        tokens.append(['IDENTIFIER',identifier])
                        identifier = ""

                # check for key word end
                elif word == 'n':
                    identifier += word
                    word = self.getNextToken()
                    if word == 'd':
                        identifier += word
                        word = self.getNextToken()
                        if word == ' ':
                            word = self.getNextToken()
                            tokens.append(['KEYWORD','end'])
                        else:
                            while word and (word!= ' '):
                                identifier += word
                                word = self.getNextToken()
                            tokens.append(['IDENTIFIER',identifier])
                            identifier = ""
                    else:
                        while word and (word!= ' '):
                            identifier += word
                            word = self.getNextToken()
                        tokens.append(['IDENTIFIER',identifier])
                        identifier = ""

            # check for while keyword
            elif word == 'w':
                identifier = word
                word = self.getNextToken()
                identifier += word
                if word == 'h':
                    word = self.getNextToken()
                    identifier += word
                    if word == 'i':
                        word = self.getNextToken()
                        identifier += word
                        if word == 'l':
                            word = self.getNextToken()
                            identifier += word
                            if word == 'e' :
                                word = self.getNextToken()
                                identifier += word
                                if word == ' ' :
                                    tokens.append(['KEYWORD','while'])
                                    word = self.getNextToken()
                                else:
                                    while word and (word!= ' '):
                                        identifier += word
                                        word = self.getNextToken()
                                    tokens.append(['IDENTIFIER',identifier])
                                    identifier = ""
                            else:
                                while word and (word!= ' '):
                                    identifier += word
                                    word = self.getNextToken()
                                tokens.append(['IDENTIFIER',identifier])
                                identifier = ""
                        else:
                            while word and (word!= ' '):
                                identifier += word
                                word = self.getNextToken()
                            tokens.append(['IDENTIFIER',identifier])
                            identifier = ""
                    else:
                        while word and (word!= ' '):
                            identifier += word
                            word = self.getNextToken()
                        tokens.append(['IDENTIFIER',identifier])
                        identifier = ""
                else:
                    while word and (word!= ' '):
                        identifier += word
                        word = self.getNextToken()
                    tokens.append(['IDENTIFIER',identifier])
                    identifier = ""

            
            # check for begin keyword
            elif word == 'b':
                identifier = word
                word = self.getNextToken()
                if word == 'e':
                    identifier += word
                    word = self.getNextToken()
                    if word == 'g':
                        identifier += word
                        word = self.getNextToken()
                        if word == 'i':
                            identifier += word
                            word = self.getNextToken()
                            if word == 'n':
                                identifier += word
                                word = self.getNextToken()
                                if word == ' ' :
                                    tokens.append(['KEYWORD','begin'])
                                    word = self.getNextToken()
                                else:
                                    while word and (word!= ' '):
                                        identifier += word
                                        word = self.getNextToken()
                                    tokens.append(['IDENTIFIER',identifier])
                                    identifier = ""
                            else:
                                while word and (word!= ' '):
                                    identifier += word
                                    word = self.getNextToken()
                                tokens.append(['IDENTIFIER',identifier])
                                identifier = ""
                        else:
                            while word and (word!= ' '):
                                identifier += word
                                word = self.getNextToken()
                            tokens.append(['IDENTIFIER',identifier])
                            identifier = ""
                    else:
                        while word and (word!= ' '):
                            identifier += word
                            word = self.getNextToken()
                        tokens.append(['IDENTIFIER',identifier])
                        identifier = ""
                else:
                    while word and (word!= ' '):
                        identifier += word
                        word = self.getNextToken()
                    tokens.append(['IDENTIFIER',identifier])
                    identifier = ""
            
            # check for program keyword
            elif word == 'p':
                identifier = word
                word = self.getNextToken()
                if word == 'r':
                    identifier += word
                    word = self.getNextToken()
                    if word == 'o':
                        identifier += word
                        word = self.getNextToken()
                        if word == 'g':
                            identifier += word
                            word = self.getNextToken()
                            if word == 'r':
                                identifier += word
                                word = self.getNextToken()
                                if word == 'a' :
                                    identifier += word
                                    word = self.getNextToken()
                                    if word == 'm' :
                                        tokens.append(['KEYWORD','program'])
                                        word = self.getNextToken()
                                    else:
                                        while word and (word!= ' '):
                                            identifier += word
                                            word = self.getNextToken()
                                        tokens.append(['IDENTIFIER',identifier])
                                        identifier = ""
                                else:
                                    while word and (word!= ' '):
                                        identifier += word
                                        word = self.getNextToken()
                                    tokens.append(['IDENTIFIER',identifier])
                                    identifier = ""
                            else:
                                while word and (word!= ' '):
                                    identifier += word
                                    word = self.getNextToken()
                                tokens.append(['IDENTIFIER',identifier])
                                identifier = ""
                        else:
                            while word and (word!= ' '):
                                identifier += word
                                word = self.getNextToken()
                            tokens.append(['IDENTIFIER',identifier])
                            identifier = ""            
                    else:
                        while word and (word!= ' '):
                            identifier += word
                            word = self.getNextToken()
                        tokens.append(['IDENTIFIER',identifier])
                        identifier = ""
                else:
                    while word and (word!= ' '):
                        identifier += word
                        word = self.getNextToken()
                    tokens.append(['IDENTIFIER',identifier])
                    identifier = ""

            # check for array keyword
            elif word == 'a':
                identifier = word
                word = self.getNextToken()
                if word == 'r':
                    identifier += word
                    word = self.getNextToken()
                    if word == 'r':
                        identifier += word
                        word = self.getNextToken()
                        if word == 'a':
                            identifier += word
                            word = self.getNextToken()
                            if word == 'y':
                                identifier += word
                                word = self.getNextToken()
                                while word and (word!= ' '):
                                    identifier += word
                                    word = self.getNextToken()
                                tokens.append(['IDENTIFIER',identifier])
                                identifier = ""
                            else:
                                while word and (word!= ' '):
                                    identifier += word
                                    word = self.getNextToken()
                                tokens.append(['IDENTIFIER',identifier])
                                identifier = ""
                        else:
                            while word and (word!= ' '):
                                identifier += word
                                word = self.getNextToken()
                            tokens.append(['IDENTIFIER',identifier])
                            identifier = ""
                    else:
                        while word and (word!= ' '):
                            identifier += word
                            word = self.getNextToken()
                        tokens.append(['IDENTIFIER',identifier])
                        identifier = ""            
                else:
                    while word and (word!= ' '):
                        identifier += word
                        word = self.getNextToken()
                    tokens.append(['IDENTIFIER',identifier])
                    identifier = ""
            

            # check for function keyword
            elif word == 'f':
                identifier = word
                word = self.getNextToken()
                if word == 'u':
                    identifier += word
                    word = self.getNextToken()
                    if word == 'n':
                        identifier += word
                        word = self.getNextToken()
                        if word == 'c':
                            identifier += word
                            word = self.getNextToken()
                            if word == 't':
                                identifier += word
                                word = self.getNextToken()
                                if word == 'i' :
                                    identifier += word
                                    word = self.getNextToken()
                                    if word == 'o' :
                                        identifier += word
                                        word = self.getNextToken()
                                        if word == 'n' :
                                            identifier += word
                                            word = self.getNextToken()
                                            if( word == ' '):

                                                tokens.append(['KEYWORD','function'])
                                                word = self.getNextToken()
                                            else:
                                                while word and (word!= ' '):
                                                    identifier += word
                                                    word = self.getNextToken()
                                                tokens.append(['IDENTIFIER',identifier])
                                                identifier = ""
                                        else:
                                            while word and (word!= ' '):
                                                identifier += word
                                                word = self.getNextToken()
                                            tokens.append(['IDENTIFIER',identifier])
                                            identifier = ""
                                    else:
                                        while word and (word!= ' '):
                                            identifier += word
                                            word = self.getNextToken()
                                        tokens.append(['IDENTIFIER',identifier])
                                        identifier = ""
                                else:
                                    while word and (word!= ' '):
                                        identifier += word
                                        word = self.getNextToken()
                                    tokens.append(['IDENTIFIER',identifier])
                                    identifier = ""            
                            else:
                                while word and (word!= ' '):
                                    identifier += word
                                    word = self.getNextToken()
                                tokens.append(['IDENTIFIER',identifier])
                                identifier = ""
                        else:
                            while word and (word!= ' '):
                                identifier += word
                                word = self.getNextToken()
                            tokens.append(['IDENTIFIER',identifier])
                            identifier = ""
                    else:
                        while word and (word!= ' '):
                            identifier += word
                            word = self.getNextToken()
                        tokens.append(['IDENTIFIER',identifier])
                        identifier = ""
                else:
                    while word and (word!= ' '):
                        identifier += word
                        word = self.getNextToken()
                    tokens.append(['IDENTIFIER',identifier])
                    identifier = ""
                
            
            # check for integer keyword
            elif word == 'i':
                identifier = word
                word = self.getNextToken()
                if word == 'n':
                    identifier += word
                    word = self.getNextToken()
                    if word == 't':
                        identifier += word
                        word = self.getNextToken()
                        if word == 'e':
                            identifier += word
                            word = self.getNextToken()
                            if word == 'g':
                                identifier += word
                                word = self.getNextToken()
                                if word == 'e' :
                                    identifier += word
                                    word = self.getNextToken()
                                    if word == 'r' :
                                        identifier += word
                                        word = self.getNextToken()
                                        if word == ' ' :
                                            tokens.append(['KEYWORD','integer'])
                                            word = self.getNextToken()
                                        else:
                                            while word and (word!= ' '):
                                                identifier += word
                                                word = self.getNextToken()
                                            tokens.append(['IDENTIFIER',identifier])
                                            identifier = ""
                                    else:
                                        while word and (word!= ' '):
                                            identifier += word
                                            word = self.getNextToken()
                                        tokens.append(['IDENTIFIER',identifier])
                                        identifier = ""
                                else:
                                    while word and (word!= ' '):
                                        identifier += word
                                        word = self.getNextToken()
                                    tokens.append(['IDENTIFIER',identifier])
                                    identifier = ""
                            else:
                                while word and (word!= ' '):
                                    identifier += word
                                    word = self.getNextToken()
                                tokens.append(['IDENTIFIER',identifier])
                                identifier = ""            
                        else:
                            while word and (word!= ' '):
                                identifier += word
                                word = self.getNextToken()
                            tokens.append(['IDENTIFIER',identifier])
                            identifier = ""
                    else:
                        while word and (word!= ' '):
                            identifier += word
                            word = self.getNextToken()
                        tokens.append(['IDENTIFIER',identifier])
                        identifier = ""
                else:
                    while word and (word!= ' '):
                        identifier += word
                        word = self.getNextToken()
                    tokens.append(['IDENTIFIER',identifier])
                    identifier = ""


            # this checks for identifiers satisfying Regular Expression letter(letter+digit)* & generates token for them
            elif re.match('[a-z]',word) or re.match('[A-Z]',word):
                id = word
                word = self.getNextToken()
                while re.match('[a-z]',word) or re.match('[A-Z]',word) or re.match('[0-9]',word) or word==" " or word == "\n":
                    
                    # this checks for whitespaces or newlines after one or more  identifiers
                    if( word == " " or word == "\n"  ):
                        break
                    # this checks for not accepting identifiers having more than 8 characters
                    elif len(id) > 8:
                        print("invalid")
                        id = " "
                        break
                    else:
                        id += word
                        word = self.getNextToken()
                
                # it excludes words having length more than 8 characters
                if(len(id) <= 8):
                    tokens.append(['IDENTIFIER',id])
                word = self.getNextToken()
            
            # this checks for unsigned integers
            elif re.match('[0-9]',word):
                integer = " "
                integer  = word
                word = self.getNextToken()
                while(re.match('[0-9]',word) or word == "E" or word == "." ):
                    if ( re.match('[0-9]',word) ):
                        integer  += word
                        word = self.getNextToken()
                    elif word == "E":
                        integer  += word
                        word = self.getNextToken()

                        if ( re.match('[0-9]',word) is None and  word != "+" and  word != "-" and word != " " and word != "\n"):
                            integer = " "
                            print("invalid")
                            word = self.getNextToken()
                            while( word != " " or word != "\n" ):
                                word = self.getNextToken()
                                if(word == " " or word == "\n" ):
                                    break
                        if(word == " " or word == "\n"):
                            integer = " "
                            print("invalid")
                            word = self.getNextToken()
                        
                        while ( re.match('[0-9]',word) or  word == "+" or  word == "-"):
                            if(re.match('[0-9]',word)):
                                integer  += word
                                word = self.getNextToken()
                                while(re.match('[0-9]',word)):
                                    integer  += word
                                    word = self.getNextToken()
                                if(re.match('[0-9]',word) is None and word != " " and word != "\n"):
                                    integer = " "
                                    print("invalid")
                                    word = self.getNextToken()
                                    while( word != " " or word != "\n" ):
                                        word = self.getNextToken()
                                        if(word == " " or word == "\n" ):
                                            break
                            elif word == "+":
                                integer  += word
                                word = self.getNextToken()
                                while(re.match('[0-9]',word)):
                                    integer  += word
                                    word = self.getNextToken()

                                if(word == " " or word == "\n"):
                                    integer  += word
                                    word = self.getNextToken()
                                elif(re.match('[0-9]',word) is None and word != " " and word != "\n"):
                                    integer = " "
                                    print("invalid")
                                    word = self.getNextToken()
                                    while( word != " " or word != "\n" ):
                                        word = self.getNextToken()
                                        if(word == " " or word == "\n" ):
                                            break
                            elif word == "-":
                                integer  += word
                                word = self.getNextToken()
                                while(re.match('[0-9]',word)):
                                    integer  += word
                                    word = self.getNextToken()

                                if(word == " " or word == "\n"):
                                    integer  += word
                                    word = self.getNextToken()
                                elif(re.match('[0-9]',word) is None and word != " " and word != "\n"):
                                    integer = " "
                                    print("invalid")
                                    word = self.getNextToken()
                                    while( word != " " or word != "\n" ):
                                        word = self.getNextToken()
                                        if(word == " " or word == "\n" ):
                                            break

                    elif word == ".":
                        integer  += word
                        word = self.getNextToken()
                        if(word == " " or word == "\n" or re.match('[0-9]',word) is None):
                            integer = " "
                            print('invalid')
                            word = self.getNextToken()
                        while(re.match('[0-9]',word)):
                            integer  += word
                            word = self.getNextToken()
                        
                # check if any invalid integer is captured
                if(integer != " " ):
                    tokens.append(["NUM",integer])
            
             # operators
            elif word == '>':
                word = self.getNextToken()
                if word == '=':
                    tokens.append(['OPERATOR','GE'])
                    word = self.getNextToken()
                else:
                    tokens.append(['OPERATOR','GT'])
                    word = self.getNextToken()
            elif word == '<':
                word = self.getNextToken()
                if word == '=':
                    tokens.append(['OPERATOR','LE'])
                    word = self.getNextToken()
                elif word == '>':
                     tokens.append(['OPERATOR','NE'])
                else:
                    word = self.getNextToken()
                    tokens.append(['OPERATOR','LT'])
                    word = self.getNextToken()
            elif word == '':
                word = self.getNextToken()
                if(word == '='):
                    word = self.getNextToken()
                    tokens.append(['OPERATOR','NE'])
                else:
                    word = self.getNextToken()
            elif word == '=':
                word = self.getNextToken()
                tokens.append(['OPERATOR','EQ'])
            elif word == '+':
                word = self.getNextToken()
                tokens.append(['OPERATOR','ADD'])
            elif word == '-':
                word = self.getNextToken()
                tokens.append(['OPERATOR','SUB'])
            elif word == '*':
                word = self.getNextToken()
                tokens.append(['OPERATOR','MUL'])
            elif word == '/':
                word = self.getNextToken()
                tokens.append(['OPERATOR','DIV'])
            elif word == '%':
                word = self.getNextToken()
                tokens.append(['OPERATOR','MOD'])
            else:
                print("not handled")
                word = self.getNextToken()


        print(tokens)
        # return created tokens
        return tokens
    
    def getNextToken(self):
        self.source_index += 1
        source_char = 'end'
        if (self.source_index < len(self.source_code)):
            source_char = self.source_code[self.source_index]
        return source_char



def main():

    # Read the Source Code from file & store in a variable
    code = ""

    # take input from below file
    with open("input.txt","r") as Input:
        code = Input.read()
    
    lex = lexer(code)
    deff = lex.tokenize()
    newlist = ""

    # save generated tokens to below file
    with open('result.txt','w+') as output:
        for defi in deff:
            output.write(str(defi))
            output.write("\n")

        output.close()

# main function
if __name__ == "__main__":
    main()
    