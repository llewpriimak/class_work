class Queue():
    '''Queue implements the FIFO principle.'''

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if (not self.isEmpty()):
            return self.queue.pop(0)
        else:
            return None

    def isEmpty(self):
        return (len(self.queue) == 0)

    def size(self):
        return len(self.queue)

    # a string representation of this stack.
    def __str__(self):
        return str(self.queue)

class stack_adapter:

    def __init__(self):
        self.queue1 = Queue()

        self.queue2 = Queue()

    def push(self, item):
        #Time element of O(1)
        self.queue1.append(item)

    def pop(self):
        #Time element of O(n)
        while not(self.queue1.isEmpty()):
            if self.queue1.size() == 1:
                final = self.queue1.dequeue()
            else:
                val = self.queue1.dequeue()
                self.queue2.enqueue(val)
        while not(self.queue2.isEmpty()):
            val = self.queue2.dequeue()
            self.queue1.enqueue(val)
        return final

    def peek(self):
        #Time element of O(n)
        while not (self.queue1.isEmpty()):
            if self.queue1.size() == 1:
                check = self.queue1.dequeue()
            else:
                val = self.queue1.dequeue()
                self.queue2.enqueue(val)
        self.queue2.enqueue(check)
        while not (self.queue2.isEmpty()):
            val = self.queue2.dequeue()
            self.queue1.enqueue(val)

        return check

# complete this method
###############################
#                             #
#   Example run of a Queue    #
#                             #
###############################

def main():
    my_queue = Queue()

    # enqueue 10
    my_queue.enqueue(10)
    print(my_queue)

    # enqueue 18
    my_queue.enqueue(18)
    print(my_queue)

    # enqueue 1024
    my_queue.enqueue(1024)
    print(my_queue)

    # dequeue()
    print("Dequeue ", my_queue.dequeue())
    print("Dequeue ", my_queue.dequeue())
    print("Dequeue ", my_queue.dequeue())
    print("Dequeue ", my_queue.dequeue())


# if __name__ == '__main__':
#     main()