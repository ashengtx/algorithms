from stack import Stack

def postfix_eval(eval_string):
    operators = '+-*/'
    operands_stack = Stack()

    for token in eval_string.split(' '):
        if token not in operators:
            operands_stack.push(float(token))
        else:
            num2 = operands_stack.pop()
            num1 = operands_stack.pop()
            res = do_cal(num1, num2, token)
            operands_stack.push(res)
    res = operands_stack.pop()

    if operands_stack.isEmpty():
        return res
    else:
        raise ValueError("eval string not legal")

def do_cal(num1, num2, token):
    if token == '*':
        return num1 * num2
    if token == '/':
        return num1 / num2
    if token == '+':
        return num1 + num2
    if token == '+':
        return num1 - num2

def main():
    print(postfix_eval("3 4 5 * +"))

if __name__ == '__main__':
    main()
