import ListQueue

class QueueStack:
    # implement a Stack using two instances of the Queue class

    def __init__():
        # implement later
        self._data = ListQueue()

    def push(self, element):
        # pushes element in the stack
        tempQueue = ListQueue()

        # use second queue to reverse the order of elements
        for index in range(self._data.size()):
            tempQueue.enqueue(self._data.dequeue())

        # reassign the data to the new queue
        self._data = tempQueue


    def pop(self):
        # pops i.e. removes the latest element from the stack and returns it
        return self._data.dequeue()
    def peep(self):
        # returns the latest element in the stack without removing it from the list
        return self._data.poll()
    
    def size(self):
        # returns the size of the stack
        return self._data.size()