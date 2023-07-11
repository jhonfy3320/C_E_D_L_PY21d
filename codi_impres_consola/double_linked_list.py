#codigo clase 

'''Type "help", "copyright", "credits" or "license" for more information.
>>> from Node import Node
>>> index = 1
>>> new_item = 'ham'
>>> head = Node(None, None)
>>> head.next = head
>>> probe = head
>>> while index > 0 and probe.nex != head:
...     probe = probe.next
>>> while probe != None:
...     print(probe.data)
...     probe = probe.previous
... 
5
4
3
2
1
>>> 
'''