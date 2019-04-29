# Non Recursive Predictive Parsing :cyclone:
##### This Program will assert that a given Input String is Parsable from the given Grammar or not ? 

## Specifications
	
* __*Grammar Used*__
 
    ```  
    - E > E + T / T  
    - T > T * F / F  
    - F > (E) / id
* __*After Removing Left Factoring & Left Recursion, Grammar used is:*__ 
	```  
    - E  > TE'  
    - E' > +TE' / ε  
    - T  > FT'
    - T' > *FT' / ε
    - F  > (E) / id
* __*Compute the FIRST & FOLLOW for above Grammar*__
* __*At last, Make the Parse Table for above Grammar*__

## Check the Input string
* Just put your string in **"Input.txt"**
* Parse Table is loaded Hard Coded using **2D Array** Data Structure
* Output would be shown on Console showing whether string is Parsable or not .

## Output
**1.** Input String  
**2.** __*Parse Table*__  
**3.** All Stack operations to maintain the productions for __*Parse Tree*__  
**4.** All __*Productions*__ which construct Parse Tree collectively.
