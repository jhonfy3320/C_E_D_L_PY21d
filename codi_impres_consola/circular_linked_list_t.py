'''>>> from Node import Node
>>> index = 1
>>> new_item = 'ham'
>>> head = Node(None, None)
>>> head.next = head
>>> probe = head
>>> while index > 0 and probe.nex != head:
...     probe = probe.next
...     index -= 1
... 

>>> head = Node(None, None)
>>> index = 1
>>> new_item = 'ham'
>>> head = Node(None, None)
>>> head.next = head
>>> probe = head
>>> while index > 0 and probe.next != head:
...     probe = probe.next
...     index -= 1
... 
>>> probe.next = Node(new_item, probe.next)
>>> print(probe.next.data)
ham
>>> '''

