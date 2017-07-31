
def bubble_sort(alist):
    for k in range(len(alist)-1, 0, -1):
        for i in range(k):
            if alist[i] > alist[i+1]:
                tmp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = tmp

def short_bubble(alist):
    for k in range(len(alist)-1, 0, -1):
        has_sorted = True
        for i in range(k):
            if alist[i] > alist[i+1]:
                has_sorted = False
                tmp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = tmp
        if has_sorted:
            break

def selection_sort(alist):
    n = len(alist)
    while n > 0:
        cur_max = 0
        for i in range(1, n):
            if alist[i] > alist[cur_max]:
                cur_max = i
        if cur_max != (n - 1):
            tmp = alist[n-1]
            alist[n-1] = alist[cur_max]
            alist[cur_max] = tmp
        n -= 1

def insert_sort(alist):
    for i in range(1, len(alist)-1):
        tmp = alist[i]
        while i > 0:
            if tmp < alist[i-1]:
                alist[i] = alist[i-1]
            else:
                break
            i -= 1
        alist[i] = tmp

def main():
    alist = [2,3,1,4,6,7,3,6,8,5,4,3]
    print(alist)
    bubble_sort(alist)
    print(alist)
    selection_sort(alist)
    print(alist)
    insert_sort(alist)
    print(alist)

if __name__ == '__main__':
    main()
