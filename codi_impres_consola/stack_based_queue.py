'''
>>> from stack_based_queue import Queue
>>> x = Queue()
>>> x.enqueue(5)
>>> x.enqueue(12)
>>> x.enqueue(26)
>>> x.enqueue(30)
>>> print(x.inbound_stack)
[5, 12, 26, 30]
>>> x.dequeue()
5
>>> print(x.inbound_stack)
[]
>>> print(x.outbound_stack)
[30, 26, 12]
>>> print(x.outbound_stack)
[30, 26, 12]
>>> x.dequeue()
12
>>> print(x.outbound_stack)
[30, 26]
>>> x.dequeue()
26
>>> print(x.outbound_stack)
[30]
>>> '''