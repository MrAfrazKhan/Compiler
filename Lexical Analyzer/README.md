# Lexical Analyzer :pencil2:

### Lexical Analyzer is one of earliest parts of a compiler, which generates tokens for source code. It is implemented with following specifications:
>* **IDENTIFIERS**: All valid identifiers under regular expression (letter)(letter | digit)*
>* **INTEGERS**: All integers including fractions, Exponents
>* **KEYWORDS**: if, do, not, else, end, program, function ,while ,then, var, procedure, of, begin, array,integer
>* **RELATIONAL OPERATORS**: =, >, <, >=, <=, <>
>* **COMMENTS**: recognized with "**{**" as start & "**}**" as end of comments.
>* **WHITE SPACES,  BLANKS, NEWLINE** 

## Method:
Insert your input source code in **"input.txt"** & then result generated in the form of tokens will be saved in **"result.txt"**.
