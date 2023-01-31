# Infix Expression Parenthesizer
 Take infix expression, add parenthesis based on PEMDAS order of operations.


# How to use:
- Enter your expression with no parenthesis, with a space between each `element`.
    - Elements include the variables represented in the expression (letters, numbers, strings) and operators
    - OPERATORS: `^*/+-`



# Current Limitations
- The program does not work with parenthesis within the input expression


# Example input/output
input:  `a * b + c * a / b - c ^ d`


output: `( ( ( a * b ) + ( ( c * a ) / b ) ) - ( c ^ d ) )`
