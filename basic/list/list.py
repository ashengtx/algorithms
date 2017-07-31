class Node():

    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def set_data(self, newdata):
        self.data = newdata

    def get_data(self):
        return self.data

    def set_next(self, next_node):
        self.next = next_node

    def get_next(self):
        return self.next

class UnorderedList():

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        cnt = 0
        cur = self.head
        while cur != None:
            cnt += 1
            cur = cur.get_next()
        return cnt

    def add(self, item):
        tmp = Node(item)
        tmp.set_next(self.head)
        self.head = tmp

    def search(self, item):
        cur = self.head
        while cur != None:
            if cur.get_data() == item:
                return True
            else:
                cur = cur.get_next()
        return False

    def remove(self, item):
        cur = self.head
        previous = None
        found = False
        while cur != None and not found:
            if cur.get_data() == item:
                found = True
            else:
                previous = cur
                cur = cur.get_next()
        if previous is None:
            self.head = cur.get_next()
        else:
            previous.set_next(cur.get_next())

    def append(self, item):
        tmp = Node(item)
        cur = self.head()
        while cur != None:
            if cur.get_next() is None:
                cur.set_next(tmp)
            else:
                cur = cur.get_next()

class OrderedList():

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        cnt = 0
        cur = self.head
        while cur != None:
            cnt += 1
            cur = cur.get_next()
        return cnt

    def add(self, item):
        tmp = Node(item)
        cur = self.head
        previous = None

        while cur != None and item > cur.get_data():
            previous = cur
            cur = cur.get_next()

        tmp.set_next(cur)
        if previous is None:
            self.head = tmp
        else:
            previous.set_next(tmp)

    def search(self, item):
        cur = self.head

        while cur != None:
            if item < cur.get_data():
                return False
            elif item == cur.get_data():
                return True
            else:
                cur = cur.get_next()

        return False

def main():
    mylist = UnorderedList()
    mylist.add(3)
    mylist.add(4)
    mylist.add(33)

    print(mylist.search(5))
    mylist.remove(3)

    # test ordered list
    mylist2 = OrderedList()
    mylist2.add(31)
    mylist2.add(77)
    mylist2.add(17)
    mylist2.add(93)
    mylist2.add(26)
    mylist2.add(54)

    print(mylist2.size())
    print(mylist2.search(93))
    print(mylist2.search(100))

if __name__ == '__main__':
    main()
