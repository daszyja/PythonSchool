# coding: utf-8

'''
Dopisz do klasy BST (drzewo binarne) dwie metody:

1). path(self,a,b) – zwracającą listę z wartościami z kolejnych
wierzchołków na ścieżce od a do b (a,b są to wartości w węzłach, jeśli takich
wartości nie ma w drzewie, to metoda powinna zwrócić listę pustą);

Wsk. Można napisać i wykorzystać metodę pathTo(self,a), która
tworzy listę ze ścieżką od korzenia do węzła z wartością a.

2). brother(self,a) – zwracającą „brata” węzła a, tj. Wartość węzła
będącego drugim potomkiem tego samego ojca co a (jeśli takowy nie istnieje, to
metoda powinna zwrócić None)'''


class binarySearchTree:

    def __init__(self, dane=None):
        self.key = dane
        self.left_node = None
        self.right_node = None

    def bst_insert_rek(self, klucz):
        if self.key == None:
            self.key = klucz
        elif klucz <= self.key:
            if self.left_node is not None:
                self.left_node.bst_insert_rek(klucz)
            else:
                self.left_node = binarySearchTree(klucz)
        else:
            if self.right_node is not None:
                self.right_node.bst_insert_rek(klucz)
            else:
                self.right_node = binarySearchTree(klucz)

    def is_key(self, value):
        if self.key is not None:
            if self.key == value:
                return True
            else:
                if value > self.key:
                    if self.right_node is not None:
                        return self.right_node.is_key(value)
                else:
                    if self.left_node is not None:
                        return self.left_node.is_key(value)

    def depth(self, value, depth=0):
        if self.key is not None:
            if self.key == value:
                return depth

            ln, rn = 9999999999, 9999999999
            if self.left_node is not None:
                ln = self.left_node.depth(value, depth + 1)
            if self.right_node is not None:
                rn = self.right_node.depth(value, depth + 1)

            if self.right_node is None and self.left_node is None:
                return 9999999999

            return min(ln, rn)

    def path(self, k1, k2):
        if self.is_key(k1) and self.is_key(k2):

            if k2 == k1:
                return [k1]
            return self._path(k1, k2)
        return []

    def _path(self, k1, k2):
        if k1 < self.key and k2 < self.key:
            return self.left_node._path(k1, k2)
        elif k1 > self.key and k2 > self.key:
            return self.right_node._path(k1, k2)
        else:
            if k1 == self.key:
                return self._path_to_node(k2)
            elif k2 == self.key:
                return list(reversed(self._path_to_node(k1)))

            ''' sciezki sie rozchodza '''
            mid = self.key
            if k1 < self.key:
                return list(reversed(self.left_node._path_to_node(k1))) + [mid] + self.right_node._path_to_node(k2)
            return list(reversed(self.right_node._path_to_node(k1))) + [mid] + self.left_node._path_to_node(k2)

    def _path_to_node(self, k):
        if self.key == k:
            return [k]
        if k > self.key:
            return [self.key] + self.right_node._path_to_node(k)
        return [self.key] + self.left_node._path_to_node(k)

    def brother(self, k):
        if self.is_key(k):
            if self.key == k:
                return None
            return self._brother(k)
        return None

    def _brother(self, k):
        if self.left_node is not None and self.left_node.key == k:
            return self.right_node.key if self.right_node is not None else None
        if self.right_node is not None and self.right_node.key == k:
            return self.left_node.key if self.left_node is not None else None

        if k > self.key:
            return self.right_node._brother(k)
        return self.left_node._brother(k)


    def printLevel(self, depth=0):
        ln, rn = [], []
        if self.key is not None and depth > 0:
            if self.left_node is not None:
                ln = self.left_node.printLevel(depth - 1)
            if self.right_node is not None:
                rn = self.right_node.printLevel(depth - 1)
        elif depth == 0:
            return [self.key]
        return ln + rn

    def printLevels_bad(self):
        for i in range(self.height()):
            print printLevel(i)

    def printLevels(self, cd=0, L=[]):
        if self.key is not None:
            if len(L) <= cd:
                L.append([])
            L[cd] += [self.key]
            if self.left_node is not None:
                self.left_node.printLevels(cd + 1, L)
            if self.right_node is not None:
                self.right_node.printLevels(cd + 1, L)
        return L

    def inorder(self):
        if self.key is not None:
            if self.left_node is not None:
                self.left_node.inorder()
            print self.key
            if self.right_node is not None:
                self.right_node.inorder()

    def preorder(self):
        if self.key is not None:
            print self.key
            if self.left_node is not None:
                self.left_node.preorder()
            if self.right_node is not None:
                self.right_node.preorder()

    def postorder(self):
        if self.key is not None:
            if self.left_node is not None:
                self.left_node.preorder()
            if self.right_node is not None:
                self.right_node.preorder()
            print self.key

    def weight(self):
        wl, wr = 0, 0
        if self.key is not None:
            wl = self.left_node.weight() if self.left_node is not None else 0
            wr = self.right_node.weight() if self.right_node is not None else 0
            return wl + wr + 1
        return 0

    def height(self):
        hl, hr = 0, 0
        if self.key is not None:
            hl = self.left_node.height() + 1 if self.left_node is not None else 0
            hr = self.right_node.height() + 1 if self.right_node is not None else 0
        return max(hl, hr)


def __setup_tree():
    bt = binarySearchTree(12)
    bt.bst_insert_rek(17)
    bt.bst_insert_rek(5)
    bt.bst_insert_rek(35)
    bt.bst_insert_rek(2)
    bt.bst_insert_rek(1)
    bt.bst_insert_rek(6)

    return bt


def test_bt():
    bt = __setup_tree()
    assert bt.path(2, 35) == [2, 5, 12, 17, 35]
    assert bt.path(5, 6) == [5, 6]
    assert bt.path(2, 6) == [2, 5, 6]
    assert bt.path(6, 2) == [6, 5, 2]

    assert bt.brother(2) == 6
    assert bt.brother(35) == None
