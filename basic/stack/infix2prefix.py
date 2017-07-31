from stack import Stack

def infix2prefix(string):
    # 可能这个用栈不好实现吧，先放着

def main():
    print("hello")
    print(infix2prefix("A + B * C + D")) # + + A * B C D
    print(infix2prefix("A * B + C * D")) # + * A B * C D
    print(infix2prefix("( A + B ) * ( C + D )")) # * + A B + C D
    print(infix2prefix("A + ( B * C ) + D")) # + + A * B C D
    print(infix2prefix("A + ( B - C + D )")) # + + A * B C D

if __name__ == '__main__':
    main()
