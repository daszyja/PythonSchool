# '''Implementacja Stack() i StackBack()
# Zadanie 1'''
#
# class Stack:
#     """docstring for Stack."""
#     def __init__(self):
#         self.items = []
#     def isEmpty(self):
#
#         return self.items == []
#     def push(self,item):
#         '''wrzucenie elementu na stos'''
#         self.items.append(item) #o1
#         return
#     def pop(self):
#         '''sciagniecie elemtu z stosu'''
#         self.items.pop()
#         return
#     def top(self):
#         '''zwracam element z gory stosu'''
#         return self.items[len(self.items)-1]
#     def size(self):
#         return len(self.items)
#
# class StackBack:
#     """docstring for Stack."""
#     def __init__(self):
#         self.items = []
#     def isEmpty(self):
#         return self.items == []
#     def push(self,item): #o1
#         '''wrzucenie elementu na stos'''
#         self.items.insert(0,item)
#         return
#     def pop(self):
#         '''sciagniecie elemtu z stosu'''  #On
#         self.items.pop(0)
#         return
#     def top(self):     #N
#         '''zwracam element z gory stosu'''
#         return self.items[0]
#     def size(self):
#         return len(self.items)
#     def wypisz(self):
#         print (self.items)
class Stack(object):
    """stos z appendem"""

    def __init__(self):
        super(Stack, self).__init__()
        self.l = []

    def push(self, o):  # O(1)
        self.l.append(o)

    def pop(self):  # O(1)
        if self.is_empty():
            return None
        return self.l.pop()

    def top(self):
        if self.is_empty():
            return None
        return self.l[-1]

    def is_empty(self):
        return len(self.l) == 0

    def size(self):
        return len(self.l)
