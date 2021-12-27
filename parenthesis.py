

def parenthesize(raw_expr: str):
    expr = raw_expr.split(" ")
    # ()^*/+-
    # make the first pass and make first check
    operand_lst = [')', '^', '*', '/', '+', '-']
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
    expr = "a * b + c * a / b - c ^ d"
    solved = "( ( ( a * b ) + ( ( c * a ) / b ) ) - ( c ^ d ) )"

    attempt = parenthesize(expr)

    print("Attempt:" + attempt + ".")

    if (attempt == solved):
        print("it worked!!")
    else:
        print("maybe next time")