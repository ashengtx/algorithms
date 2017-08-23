from stack import Stack 

def divideby2(decimal_num):
    s = Stack()

    while decimal_num > 0:
        remain = decimal_num % 2
        s.push(remain)
        decimal_num = decimal_num // 2

    string = ''
    while not s.isEmpty():
        string += str(s.pop())

    return string

def baseConverter(decimal_num, base):
    digits = "0123456789ABCDEF"
    s = Stack()

    while decimal_num > 0:
        remain = decimal_num % base
        s.push(remain)
        decimal_num = decimal_num // base
        
    string = ''
    while not s.isEmpty():
        string += digits[s.pop()]

    return string

if __name__ == '__main__':
    print(divideby2(233))
    print(baseConverter(233, 16))
    a = {}
    
