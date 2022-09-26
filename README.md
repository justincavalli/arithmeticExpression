* Implement a stack data structure from scratch. You can’t use built-in Stack APIs. You can use the built-in Array or List or your custom-built LinkedList.  The Stack class must have the following functions:
    * push(x) : pushes x in the stack. 
    * pop(): pops i.e. removes the latest element from the stack and returns it. 
    * peep(): returns the latest element from the stack without removing it from the list. 
    * size(): returns the size of the stack. 
* Given a string str that represents an arithmetic expression, evaluate the arithmetic expression.
    * The arithmetic expression can include any arithmetic operator i.e. + , - , /, *, and numeric operands i.e. any number from  (-2^31) to (2^31-1). 
    * There may be one or more white spaces between an operand and an operator. You should ignore the white spaces while scanning. 
    * For an invalid expression i.e. any operand other than numeric values, invalid operator, or division by 0, either return NaN or throw an exception. 
    * You have to use the stack you implemented in the first prompt of the assignment.

Example: 

Input: str = "10 + 20 * 2"

Output: 50

Input: str = “foo / 30 + 7”

Output: NaN

* Implement a queue data structure from scratch. You cannot use built-in Queue APIs. You can use the built-in Array or List or your custom-built LinkedList.  The Queue class must have the following functions:
    * enqueue(x) : enqueue x in the queue. 
    * dequeue(): dequeue i.e. remove and return the earliest element from the queue. 
    * poll(): returns the earliest element from the queue without removing it. 
    * size(): returns the size of the queue.  
* Implement a Stack using only two instances of the Queue class and queue operations allowed on your implemented in your queue class.
