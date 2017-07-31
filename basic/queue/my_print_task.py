from queue import Queue
import random

class Printer():
    def __init__(self, pages_per_minute):
        self.pages_per_minute = pages_per_minute
        self.cur_task = None
        self.pages = 0

    def busy(self):
        if self.cur_task is None:
            return False
        else:
            return True

    def start_next(self, new_task):
        self.cur_task = new_task
        self.pages = new_task.get_pages()

    def tick(self):
        """
        一秒打印多少页
        """
        self.pages -= self.pages_per_minute / 60
        if self.pages <= 0:
            self.cur_task = None


class Task():
    def __init__(self, cur_time):
        self.time = cur_time
        self.pages = random.randrange(1, 21)

    def get_pages(self):
        return self.pages

    def get_time(self):
        return self.time


def new_task():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False

def simulation(num_seconds, pages_per_minute):

    lab_printer = Printer(pages_per_minute)
    task_queue = Queue()
    waiting_times = []

    for cur_second in range(num_seconds):

        # 有新任务到达
        if new_task():
            task = Task(cur_second)
            task_queue.enqueue(task)

        # 如果打印机空闲，并且任务队列有任务在等待，则出队，并计算等待时间，然后执行新任务
        if not lab_printer.busy() and not task_queue.isEmpty():
            next_task = task_queue.dequeue()
            waiting_times.append(cur_second - next_task.get_time())
            lab_printer.start_next(next_task)

        # 打印机运转
        lab_printer.tick()
    average_waiting = sum(waiting_times)/len(waiting_times)

    print("average waiting %6.2f seconds, %d remain..."%(average_waiting, task_queue.size()))


for i in range(10):
    simulation(3600, 5)



