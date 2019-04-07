import re
import time 

# Author   AHMAD AFRAZ KHAN
# Reg # :  2015-CS-27

# Search for Keywords through Hash Table & Hash Function

# KEYWORDS:      if, do, not, else, end, program,
#                function ,while ,then, var,
#                procedure, of, begin, array, integer
 


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
        
        HashT = HashTable()    
        HashT[10]="begin"
        HashT[11]="integer"
        HashT[12]="if"
        HashT[13]="else"
        HashT[14]="function"
        HashT[15]="var"
        HashT[16]="do"
        HashT[17]="not"
        HashT[18]="end"
        HashT[19]="program"
        HashT[20]="while"
        HashT[21]="then"
        HashT[22]="procedure"
        HashT[23]="of"
        HashT[24]="array"

        # loop through each  word in source code to generate tokens 
        while (1):
            
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
            elif re.match('[a-z]',word) or re.match('[A-Z]',word):
                identifier = word
                word = self.getNextToken()
                while(re.match('[a-z]',word) or re.match('[A-Z]',word) or re.match('[0-9]',word)):
                    identifier += word
                    word = self.getNextToken()
                
                if(word == ' '):
                    found = False
                    for x in range(10,24):
                        if(HashT[x] == identifier):
                            found = True
                            tokens.append(['KEYWORD',HashT[x]])

                    if(found == False):
                        tokens.append(['IDENTIFIER',identifier])
                    
                    identifier = ""
                    word = self.getNextToken()





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


class HashTable:
    def __init__(self):
        self.size = 15
        self.keys = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,data):
      hashvalue = self.hashfunction(key,len(self.keys))

      if self.keys[hashvalue] == None:
        self.keys[hashvalue] = key
        self.data[hashvalue] = data
      else:
        if self.keys[hashvalue] == key:
          self.data[hashvalue] = data  #replace
        else:
          nextslot = self.rehash(hashvalue,len(self.keys))
          while self.keys[nextslot] != None and \
                          self.keys[nextslot] != key:
            nextslot = self.rehash(nextslot,len(self.keys))

          if self.keys[nextslot] == None:
            self.keys[nextslot]=key
            self.data[nextslot]=data
          else:
            self.data[nextslot] = data #replace

    def hashfunction(self,key,size):
         return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def get(self,key):
      startslot = self.hashfunction(key,len(self.keys))

      data = None
      stop = False
      found = False
      position = startslot
      while self.keys[position] != None and  \
                           not found and not stop:
         if self.keys[position] == key:
           found = True
           data = self.data[position]
         else:
           position=self.rehash(position,len(self.keys))
           if position == startslot:
               stop = True
      return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)


def main():

    # # Read the Source Code from file & store in a variable
    code = ""

    # take input from below file
    with open("Input.txt","r") as Input:
        code = Input.read()
    
    lex = lexer(code)
    deff = lex.tokenize()
    newlist = ""

    # save generated tokens to below file
    with open('Result.txt','w+') as output:
        for defi in deff:
            output.write(str(defi))
            output.write("\n")

        output.close()
    

# main function
if __name__ == "__main__":
    main()
    
