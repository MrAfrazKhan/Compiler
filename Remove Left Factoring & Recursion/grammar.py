

# Author: AFRAZ KHAN
# Reg No: 2015-CS-27


lookAhead = ''
inputIndex = 0
inputStr = ''
source_index = 0

# input string is captured here
with open("inputStr.txt","r") as INPUT2:
    inputStr = INPUT2.read()
    INPUT2.close()


def main():

    # Read the Source grammar from file & store in a variable
    grammer = ""
    Terminal = ''
    prods = ''

    # New grammar with no left recursion & left factoring is kept in below variable
    RealGrammar = []


    # take grammer from below file
    with open("grammar.txt","r") as Input:
        grammer = Input.read()
        Input.close()

    
    # productions are manipulated for their results
    grammerArray = grammer.split('>')
    T1 = grammerArray[0]
    Terminal = T1.strip()
    prods1 = grammerArray[1].split('/')
    prods = []

    ind = 0
    for stR in prods1:
        str1 = stR.strip()
        prods.insert(ind,str1)
        ind += 1

    factors = []
    
    common = ''
    i = 0
    unCommon = []

    # check for factors in grammer
    for STR in prods:
        strs = None

        if(Terminal in STR):
            strs = STR.split(Terminal)
            if(strs[0] == ''):
                strs = None
        if (strs is not None and i == 0 ):
            common = strs[0]
            i += 1
            unCommon.insert(0,strs[1])
        elif strs is not None:
            if(common == strs[0]):
                unCommon.insert(i,strs[1])
                i += 1
        else:
            common = " "
            if(common in STR):
                unCommon.insert(i,strs[1])
                i += 1
    
    TerminalDash = Terminal + '\''
    if(i == (len(prods))):
        RealGrammar.insert(0,[Terminal,common+TerminalDash])

        DashProd = ''
        j = 0
        for sTR in unCommon:
            if(sTR == ''):
                sTR = 'ε'
            if(j == 0):
                DashProd = sTR
                j += 1
            else:
                DashProd += '/'+sTR


        print(RealGrammar)
        RealGrammar.insert(1,[TerminalDash,DashProd])
        print("Left Factoring removed.")
        
        # string parse start here
        E(RealGrammar)

    # left recursion removel
    else:
        alphas = []
        betas = []

        i = 0
        j = 0
        for STR in prods:
            strs = None

            if(Terminal in STR):
                strs = STR.split(Terminal)
                alphas.insert(i,strs[1])
                i += 1
            else:
                betas.insert(j,STR)
                j += 1

        betaStr = ""
        alphaStr = ""

        if( not betas):
            betaStr = TerminalDash


        k = 0
        l = 0
        for sTr in betas:
            if k ==0 :
                betaStr = sTr+TerminalDash
                k += 1
            else:
                betaStr += "/"+sTr+TerminalDash


        for strq in alphas:
            if(l == 0):
                alphaStr = strq+TerminalDash
                l +=1
            else:
                alphaStr += "/"+strq+TerminalDash
        
        alphaStr += '/ε'

        RealGrammar.insert(0,[Terminal,betaStr])
        RealGrammar.insert(1,[TerminalDash,alphaStr])

        print(RealGrammar)
        
        # string parse start here
        E(RealGrammar)    
        print('Recursion removed')

# First Production
def E(RealGram):
    
    firstProd  = RealGram[0][1]
    prods3 = firstProd.split('E\'')
    
    tokens = list(prods3[0])

    lookAhead = getNextchar()
    if(lookAhead == tokens[0]):
        for char in tokens:
            if(lookAhead == char):
                match(char)
    
    E_(RealGram)
    
    
# Second Production    
def E_(RealGram):
    
    secondProd = RealGram[1][1]
    prods3 = secondProd.split('/')
    prods4 = prods3[0].split('E\'')
    
    tokens = list(prods4[0])
    
    if(lookAhead == tokens[0]):
        for char in tokens:
            if(lookAhead == inputStr[len(inputStr)-1]):
                print("String is parsed")
            if(lookAhead == char):
                match(char)
    else:
        return


def match(char):
    global lookAhead
    if lookAhead == char:
        lookAhead = getNextchar()
    else:
        print("Error in Parsing . . . ")
    
def getNextchar():
    global source_index
    source_char = 'end'
    if source_index < len(inputStr):
        source_char = inputStr[source_index]
        source_index += 1
    return source_char




# main function
if __name__ == "__main__":
    main()


    