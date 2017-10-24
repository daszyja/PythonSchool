# Implementacja stosu jako Abstrakcyjnej Struktury Danych (ADT-Abstract Data Type)

class Stack_01:
    """Implementacja stosu za pomoca listy Pythona, czyli klasycznie tablicy"""
    def __init__(self):
        """iicjalizacja"""
        self.items = []
    def isEmpty(self):
        """sprawdzenie czy stos jest pusty"""
        return self.items == []
    def push(self, item):
        """wlozenie elementu na stos"""
        self.items.append(item)
    def pop(self):
        """sciagniecie eleemntu ze stosu"""
        return self.items.pop()
    def top(self):
        """zwrocenie eleemntu ze szczytu stosu"""
        return self.items[len(self.items)-1]
    def size(self):
        """zwraca rozmiar stosu"""
        return len(self.items)
