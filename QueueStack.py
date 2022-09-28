# Name: Justin Cavalli
# Date: last edit 9/27/2022
# Description: This program implements the functionality of a Stack data
#              structure using two ListQueues

import ListQueue

class QueueStack:
    # implement a Stack using two instances of the Queue class

    def __init__(self):
        # implement later
        self._data = ListQueue.ListQueue()

    def push(self, element):
        # pushes element in the stack
        
        # add the element to a new queue
        tempQueue = ListQueue.ListQueue()
        tempQueue.enqueue(element)

        # reverse the order utilizing these two queues
        while not self._data.is_empty():
            tempQueue.enqueue(self._data.dequeue())

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