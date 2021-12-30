# William Craig
# Simple Infix Parenthesizer

def parenthesize(raw_expr: str):
    expr = raw_expr.split(" ")
    # ()^*/+-
    # make the first pass and make first check
    operand_lst = ['^', '*', '/', '+', '-']
    for op in operand_lst:
        i = 0
        while i < len(expr):
            if expr[i] == op:
                expr[i] = "( " + expr[i-1] + " " + expr[i] + " " + expr[i+1] + " )"
                del expr[i+1]
                del expr[i-1]
            else:
                i += 1


    return expr[0]


if __name__ == '__main__':
    # please enter the expression as a string with a space between each element ( element being variable, number, or valid operator(['^', '*', '/', '+', '-']))
    expr = "a * b + c * a / b - c ^ d"
    print(f"input:  {expr}\n")
    print(f"output: {parenthesize(expr)}\n")