import sys

class listStack():
    def __init__(self):
        # a python list stores the data in the stack
        self._stack = []

    def push(self, x):
        # pushes x in the stack
        self._stack.append(x)

    def pop(self):
        # pops i.e. removes the last element from the stack and returns it

        if(self.__is_empty__()):
            # error if the stack is empty
            raise Exception('the stack is empty')
        else:
            return self._stack.pop()


    def peep(self):
        # returns the latest element from the stack without removing it from the list

        if(self.__is_empty__()):
            # error if the stack is empty
            raise Exception('the stack is empty')
        else:
            return self._stack[self.size()-1]

    def size(self):
        # returns the size of the stack
        return len(self._stack)

    def __is_empty__(self):
        # returns true if the stack is empty
        return len(self._stack) == 0
         
def main():
    print(sys.argv[1])

if __name__ == "__main__":
    main()