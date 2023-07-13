'''
Queue basada en nodos
Python 3.10.9 (main, Mar  1 2023, 18:23:06) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from node_based_queue import Queue
>>> food = Queue()
>>> food.enqueue('eggs')
>>> food.enqueue('ham')
>>> food.enqueue('spam')
>>> food.head
<node_based_queue.TwoWayNode object at 0x7fad1a446680>
>>> food.head.data
'eggs'
>>> food.head.next.data
'ham'
>>> food.tail.data
'spam'
>>> food.tail.previous.data
'ham'
>>> food.count
3
>>> food.dequeue()
'eggs'
>>> food.head.data
'ham'
>>> '''