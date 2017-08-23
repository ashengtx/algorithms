from stack import Stack 

def infix2Postfix(infix_expr):
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1

    token_list = infix_expr.split(' ')

    output_list = []
    operator_stack = Stack()

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            # 直接输出
            output_list.append(token)
        elif token == '(':
            # 直接入栈
            operator_stack.push(token)
        elif token == ')':
            # 出栈至output_list，直到遇到'('
            top = operator_stack.pop()
            while top != '(':
                output_list.append(top)
                top = operator_stack.pop()
        else:
            # 和栈顶的操作符比较优先级，若高于，则入栈，若低于，则先出栈，再入栈
            while (not operator_stack.isEmpty()) and prec[token] < prec[operator_stack.peek()]:
                top = operator_stack.pop()
                output_list.append(top)
            operator_stack.push(token)

    while not operator_stack.isEmpty():
        output_list.append(operator_stack.pop())

    return ' '.join(output_list)

def infix2Prefix(infix_expr):
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1

    token_list = infix_expr.split(' ')

    output_list = []
    operator_stack = Stack()

    for token in token_list:
        # todo 

    while not operator_stack.isEmpty():
        output_list.append(operator_stack.pop())

    return ' '.join(output_list)

if __name__ == '__main__':

    print(infix2Postfix("A + B * C + D")) # A B C * D + +
    print(infix2Postfix("A * B + C * D")) # A B * C D * +
    print(infix2Postfix("( A + B ) * ( C + D )")) # A B + C D + *

