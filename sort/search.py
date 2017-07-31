
def binary_search(alist, item):

    if len(alist) == 0:
        return False

    found = False

    left = 0
    right = len(alist) - 1

    """
    # 用了可以提升一点效率
    if item < alist[left] or item > alist[right]:
        return found
    elif item == alist[left] or item == alist[right]:
        found = True"""

    # 核心
    while not found and left <= right:
        mid = (left+right)//2
        if item == alist[mid]:
            found = True
        elif item > alist[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return found

def binary_search_recur(alist, item):

    if len(alist) == 0:
        return False

    found = False
    mid = len(alist) // 2

    if item == alist[mid]:
        return True
    elif item > alist[mid]:
        return binary_search_recur(alist[mid+1:], item)
    else:
        return binary_search_recur(alist[:mid], item)

def binary_search_recur_2(alist, item, start, end):

    if start == end:
        return item == alist[start]

    mid = (start + end) // 2

    if item == alist[mid]:
        return True
    elif item > alist[mid]:
        return binary_search_recur_2(alist, item, mid+1, end)
    else:
        return binary_search_recur_2(alist, item, start, mid)

def main():
    alist = [1,2,3,4,5]
    print(binary_search(alist, 3))
    print(binary_search(alist, 3))
    print(binary_search_recur(alist, 14))
    print(binary_search_recur(alist, 14))
    print(binary_search_recur_2(alist, 14, 0, len(alist)-1))
    print(binary_search_recur_2(alist, 5, 0, len(alist)-1))

if __name__ == '__main__':
    main()
