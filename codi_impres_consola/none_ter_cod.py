'''
>>> from Node import Node
>>> head = None
>>> for count in range(1, 6):
...     head = Node(count, head)
... 
>>> while head != None:
...     print(head.data)
...     head = head.next
... 
5
4
3
2
1
>>> probe = head
>>> while probe != None:
...     print(probe.data)
...     probe = probe.next
... 
>>> probe = head
>>> target_item = 2
>>> while probe != None and target_item != probe.data:
...     probe = probe.next
... 
>>> if probe != None:
...     print(f'target item {target_item} has been fount')
... else:
...     print(f'target item {target_item} is not  in the linked list')
... 
target item 2 is not  in the linked list
>>> probe = head
>>> target_item = 3
>>> new_item = 'z'
>>> 
>>> while probe != None and target_item != probe.data:
...     probe = probe.next
... 
>>> if probe != None:
...    probe.data = new_item
...    print(f'{new_item} replaced the old value in the node number {target_item}')
... else:
...     print(f'target item {target_item} is not  in the linked list')
... 
target item 3 is not  in the linked list
>>> head = Node('f', head)
>>> new_node = Node('K')
>>> if head is None:
...     head = new_node
... else:
...     probe = head
...     while probe.next != None:
...             probe = probe.next
...     probe.next = new_node
... 
>>> removed_item = head.data
>>> head = head.next
>>> print(removed_item)
f
>>> removed_item = head.data
>>> if head.next is Node:
...     head = None
... else:
...     probe = head
...     while probe.next.next != None:
...             probe = probe.next
...     removed_item = probe.next.data
...     probe.next = None
... 

>>> removed_item = head.data
>>> head = head.next
>>>     head = None

>>> new_item = input('enter new item: ')
enter new item: 10
>>> index = int(input('enter de position to insert the new item: '))
enter de position to insert the new item: 3
>>> if head is None or index < 0:
...    head = Node('py', head)
... else:
...    probe = head
...    while index > 1 and probe.next != None'''