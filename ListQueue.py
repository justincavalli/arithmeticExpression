class ListQueue:

    # queue will need to be resized, assign an initial size
    INITIAL_SIZE = 10

    def __init__(self):
        # a python list stores the data in the queue
        self._queue = [None] * self.INITIAL_SIZE
        self._size = 0
        self._fIndex = 0

    def enqueue(self, x):
        # enqueues x in the queue

        # if the queue is full, resize the max list size
        if len(self._queue) == self._size:
            # double the size
            self._resize(2)
        
        # find the index of where to place the new element
        endOfQueue = (self._fIndex + self._size) % len(self._queue)
        self._queue[endOfQueue] = x

        # update the size
        self._size += 1


    def dequeue(self):
        # dequeue i.e. remove and return the earliest element from the queue
        if self.is_empty():
            raise Exception("Queue is empty")
        element = self._queue[self._fIndex]
        self._queue[self._fIndex] = None
        # increment the front index, accounting for wrapping to the beginning of the list
        self._fIndex = (self._fIndex + 1) % len(self._queue)

        # update the size and return
        self._size -= 1
        return element 


    def poll(self):
        # returns the earliest element from the queue without removing it
        if self.is_empty():
            raise Exception("Queue is empty")
        return self._queue[self._fIndex]

    def size(self):
        # returns the size of the queue
        return self._size

    def is_empty(self):
        # returns true if the queue is empty
        return self._size == 0

    def _resize(self, multiplier):
        # make new queue with size based on the multiplier
        newQueue = [None] * (multiplier * len(self._queue))

        # place all elements in queue into the new queue
        for index in range(self._size):
            newQueue[index] = self._queue[(self._fIndex + index) % len(self._queue)]

        self._queue = newQueue
        self._fIndex = 0