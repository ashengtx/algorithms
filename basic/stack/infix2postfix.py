from stack import Stack

def infix2postfix(string):
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1

    output_list = []
    operator_stack = Stack()
    for token in string.split(" "):
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
            output_list.append(token)
        elif token == '(':
            operator_stack.push(token)
        elif token == ')':
            top = operator_stack.pop()
            while top != '(':
                output_list.append(top)
                top = operator_stack.pop()
        else:
            while not operator_stack.isEmpty() and prec[token] <= prec[operator_stack.peek()]:
                output_list.append(operator_stack.pop())
            operator_stack.push(token)
    while not operator_stack.isEmpty():
        output_list.append(operator_stack.pop())
    return ' '.join(output_list)

def main():
    print("hello")
    print(infix2postfix("A + B * C + D"))
    print(infix2postfix("A * B + C * D"))
    print(infix2postfix("( A + B ) * ( C + D )"))
    print(infix2postfix("A + ( B * C ) + D"))

if __name__ == '__main__':
    main()
