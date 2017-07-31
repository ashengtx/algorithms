
def sum_recur(numlist):
    if len(numlist) == 1:
        return numlist[0]
    return numlist[0]+sum_recur(numlist[1:])

def int2str(num):
    conv_string = "0123456789"
    if num < 10:
        return conv_string[num]
    return int2str(num//10) + conv_string[num%10]

def int2str_base(num, base):
    conv_string = "0123456789ABCDEF"
    if num < base:
        return conv_string[num]
    return int2str(num//base) + conv_string[num%base]

def str_reverse(string):
    # 考虑字符为空的情况，故因<=1
    if len(string) <= 1:
        return string
    return str_reverse(string[1:]) +string[0]

def palindrome_chekcer(string):
    letter = 'abcdefghijklmnopqrstuvwxyz'

    string_clean = ""
    for ch in string.lower():
        if ch in letter:
            string_clean += ch

    def checker(string):
        if len(string) <= 1:
            return True
        if string[0] == string[-1]:
            return checker(string[1:-1])
        else:
            return False
    return checker(string_clean)


def main():
    print(sum_recur([1,2,3,4,5]))
    print(int2str(12345))
    print(int2str_base(12345, 16))
    print(str_reverse('good'))
    print(palindrome_chekcer('Live not on evil'))
    print(palindrome_chekcer('Reviled did I live, said I, as evil I did deliver'))

if __name__ == '__main__':
    main()
