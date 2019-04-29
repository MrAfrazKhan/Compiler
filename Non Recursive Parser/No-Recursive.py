import numpy
import time

# Author: AFRAZ KHAN
# Reg No: 2015-CS-27




def main():

    InputStr = ""
    with open("Input.txt","r") as In:
        InputStr = In.read()
        print("\nInput String: "+ InputStr+"\n")
        In.close()

    Input = []
    for chr in InputStr:
        if(chr.isalpha()):
            Input.append('id')
        else:
            Input.append(chr)
    
    Input.append('$')

    
    # here Parse Table is stored
    ParseTable = numpy.empty((6,7),dtype=object)
    
    time.sleep(1)
    print("Parse Table:\n")
    # setting Non-Terminals
    ParseTable[0][0] = None
    ParseTable[1][0] = 'E'
    ParseTable[2][0] = 'E\''
    ParseTable[3][0] = 'T\''
    ParseTable[4][0] = 'T'
    ParseTable[5][0] = 'F'

    # setting Terminals
    ParseTable[0][1] = '+'
    ParseTable[0][2] = '*'
    ParseTable[0][3] = 'id'
    ParseTable[0][4] = '('
    ParseTable[0][5] = ')'
    ParseTable[0][6] = '$'

    # setting productions in ParseTabels
    ParseTable[1][3] = 'E>TE\''
    ParseTable[1][4] = 'E>TE\''

    ParseTable[2][1] = 'E\'>+TE\''
    ParseTable[2][5] = 'E\'>ε'
    ParseTable[2][6] = 'E\'>ε'

    ParseTable[3][1] = 'T\'>ε'
    ParseTable[3][2] = 'T\'>*FT\''
    ParseTable[3][5] = 'T\'>ε'
    ParseTable[3][6] = 'T\'>ε'

    ParseTable[4][3] = 'T>FT\''
    ParseTable[4][4] = 'T>FT\''
    
    ParseTable[5][3] = 'F>id'
    ParseTable[5][4] = 'F>(E)'

    # Final Parse Table would be as follows:
    #     [[ None '+'       '*'      'id'    '('     ')'    '$' ]
    #     [ 'E'    None      None    "E>TE'" "E>TE'"  None   None ]
    #     [ "E'"  "E'>+TE'"  None     None    None   "E'>ε" "E'>ε" ]
    #     [ "T'"  "T'>ε"    "T'>*FT'" None    None   "T'>ε" "T'>ε" ]
    #     [ 'T'    None      None    "T>FT'" "T>FT'"  None   None ]
    #     [ 'F'    None      None    'F>id'  'F>(E)'  None   None] ]


    print(ParseTable)
    StackInput = '$'
    Productions = []
    STACK = []
    STACK.append(StackInput)
    STACK.append('E')
    NotParsable = False
    i = 0


    print("\n")
    for strr in Input:
        while(TOP(STACK) != strr):
            if TOP(STACK) == 'E':
                # print('in T')
                if(strr == 'id' or strr == '('):
                    STACK.pop()
                    STACK.append('E\'')
                    STACK.append('T')
                    Productions.append(ParseTable[1][3])
                else:
                    NotParsable = True
                    break
            elif(TOP(STACK) == "E\'"):
                # print('in E\'')
                if(strr == '+'):
                    STACK.pop()
                    STACK.append('E\'')
                    STACK.append('T')
                    STACK.append('+')
                    Productions.append(ParseTable[2][1])
                elif(strr == ')' or strr == '$'):
                    STACK.pop()
                    Productions.append(ParseTable[2][5])
                else:
                    NotParsable = True
                    break
            elif(TOP(STACK) == "T\'"):
                # print('in T\'')
                if(strr == '+' or strr == ')' or strr == '$'):
                    STACK.pop()
                    Productions.append(ParseTable[3][1])
                elif(strr == '*'):
                    STACK.pop()
                    STACK.append('T\'')
                    STACK.append('F')
                    STACK.append('*')
                    Productions.append(ParseTable[3][2])
                else:
                    NotParsable = True
                    break
            elif(TOP(STACK) == 'T'):
                # print('in Taya')
                if(strr == 'id' or strr == '('):
                    STACK.pop()
                    STACK.append('T\'')
                    STACK.append('F')
                    Productions.append(ParseTable[4][3])
                else:
                    NotParsable = True
                    break
            elif TOP(STACK) == 'F':
                # print('in F')
                if(strr == 'id'):
                    STACK.pop()
                    STACK.append('id')
                    Productions.append(ParseTable[5][3])
                elif strr == '(':
                    STACK.pop()
                    STACK.append(')')
                    STACK.append('E')
                    STACK.append('(')
                    Productions.append(ParseTable[5][4])
                else:
                    NotParsable = True
                    break
            elif TOP(STACK) == '$':
                NotParsable = True
                break
            
            print(STACK)
            time.sleep(1)

            
            
            
        if TOP(STACK) == '+':
            STACK.pop()
            Input = Input[::-1]
            Input.pop()
            Productions.append(ParseTable[2][1])
        elif TOP(STACK) == '*':
            STACK.pop()
            Input = Input[::-1]
            Input.pop()
            Productions.append(ParseTable[3][2])
        elif TOP(STACK) == 'id':
            STACK.pop()
            Input = Input[::-1]
            Input.pop()
            Productions.append(ParseTable[5][3])
        elif TOP(STACK) == '(':
            STACK.pop()
            Input = Input[::-1]
            Input.pop()
            Productions.append(ParseTable[5][4])
        elif TOP(STACK) == ')':
            STACK.pop()
            Input = Input[::-1]
            Input.pop()
            Productions.append(ParseTable[5][4])

        Input = Input[::-1]
        if(NotParsable == True):
            break
    
    if(NotParsable == True):
        print('String is not Parsable')
    else:
        print('String is Parsable')

    print("\n Productions: \n")
    print(Productions)

    #print(ParseTable) 


def TOP(stack):
    count = len(stack)
    top = stack[count-1]
    return top


# main function
if __name__ == "__main__":
    main()


    