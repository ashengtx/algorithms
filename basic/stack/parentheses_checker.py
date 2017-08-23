from stack import Stack

def parChecker(symbolString):
    s = Stack()
    for c in symbolString:
        if c == '(':
            s.push(c)
        else:
            if s.isEmpty():
                return False
            else:
                s.pop()
    if s.isEmpty():
        return True
    else:
        return False

def parChecker_general(symbolString):
    def matches(open_sb, close_sb):
        opens = '([{'
        closes = ')]}'
        return opens.index(open_sb) == closes.index(close_sb)

    s = Stack()
    for c in symbolString:
        if c in '([{':
            s.push(c)
        else:
            if s.isEmpty():
                return False
            else:
                top = s.pop()
                if not matches(top, c):
                    return False
    if s.isEmpty():
        return True
    else:
        return False

if __name__ == '__main__':
    print(parChecker('((()(()())))'))
    print(parChecker_general('((([})(()())))'))
