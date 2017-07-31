from queue import Queue 

def hot_potato(name_list, num):

    name_queue = Queue()
    for name in name_list:
        name_queue.enqueue(name)

    while name_queue.size() > 1:
        for _ in range(num):
            name_queue.enqueue(name_queue.dequeue())
        name_queue.dequeue()
    return name_queue.dequeue()

def main():
    name_list = ['a', 'b', 'c', 'd', 'e', 'f']
    print(hot_potato(name_list, 2))

if __name__ == '__main__':
    main()
