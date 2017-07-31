from deque import Deque

def pld_checher(string):

    char_deque = Deque()
    for c in string:
        char_deque.add_front(c)
    while char_deque.size() > 1:
        if string_qdeue.remove_front() != char_deque.remove_rear():
            return False
    return True

def main():
    print(pld_checher("abdba"))
    print(pld_checher("abdbab"))

if __name__ == '__main__':
    main()
