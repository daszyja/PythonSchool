# coding: utf-8
'''
- inorder() - wypisuje drzewo w porządku Inorder;
- preorder() - wypisuje drzewo w porządku Preorder;
- postorder() - wypisuje drzewo w porządku Postorder;
- height() - zwraca wysokość drzewa;
- weight() - zwraca liczbę wierzchołków w drzewie (nie liczymy tutaj węzłów pustych, tylko rzeczywistych);
- isKey(key) - zwraca wartość logiczną - czy podany key jest kluczem w drzewie;
- depth(key) - zwraca głębokość wierzchołka, którego klucz równy jest
key - jeśli takiego wierzchołka w drzewie nie ma, to zwraca stosowną
informację o tym;
- isLeaf(key) - zwraca wartość logiczną - czy podany key jest liściem w drzewie;
- isLeaf2(key) - zwraca wartość logiczną - czy podany key jest liściem w drzewie - tym razem zakładamy, że w drzewie wartości kluczy mogą się powtarzać, przy czym wszystkie wartości w lewym poddrzewie są <= korzeń, a w prawym > korzeń;
- leafsnr() - zwraca liczbę wierzchołków o stopniu 0 (czyli liści);
- leafs() - wypisuje wszystkie liście;
'''

'''
II CZĘŚĆ
- listleafs() - tworzy listę liści;
- printlevel(k) - wypisuje elementy(klucze) drzewa z poziomu
k, tj. wszystkie wierzchołki o głębokości k, w kolejności od lewej do
prawej;
- printlevels() -
wypisuje elementy(klucze) drzewa poziomami, tj. najpierw korzeń, później
elementy z pierwszego poziomu od strony lewej, później z drugiego od
strony lewej itd. - zawsze na każdym poziomie "od lewej do prawej" (to
zadanie jest chyba najtrudniejsze i można je napisać z wykorzystaniem
stosu).
- __str__(), która zaprezentuje drzewo graficznie - tak jak jest to widoczne na załączonym przykładzie;
- maxBranch() - wypisuje klucze z najdłuższej gałęzi (kolejno od korzenia do liścia lub od liścia do korzenia);
- next(x), prev(x) - zwraca odpowiednio kolejny i poprzedni element w drzewie względem x (tj. takie, że nie istnieją w drzewie T elementy a, b takie, że T.prev(x)<a<x oraz x<b<T.next(x)), lub None, jeśli x nie jest kluczem w drzewie (lub jeśli next/prev nie istnieją).
'''


class binarySearchTree:
    """Klasa drzewo binarne - prosze zwrocic uwage na roznice w stosunku do poprzedniej wersji"""

    def __init__(self, dane=None):
        self.key = dane
        self.left_node = None
        self.right_node = None

    def bst_insert_nr(self, klucz):
        if self.key is None:
            self.key = klucz
        else:
            z = binarySearchTree(klucz)  # teraz jest to drzewo binarne - poprzednio byl to wezel - Node
            y = None
            x = self
            while (x is not None):
                y = x
                if (z.key < x.key):
                    x = x.left_node
                else:
                    x = x.right_node
            if (z.key < y.key):
                y.left_node = z
            else:
                y.right_node = z

    def bst_insert_rek(self, klucz):
        if self.key == None:
            self.key == klucz
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
            if self.left_node is not None:
                return self.left_node.is_key(value) or self.right_node.is_key(value) if self.right_node is not None else False
            return self.right_node.is_key(value) if self.right_node is not None else False

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

            return min(ln,rn)

    def printLevel(self, depth=0):
        ln, rn = [],[]
        if self.key is not None and depth > 0:
            if self.left_node is not None:
                ln = self.left_node.printLevel(depth -1)
            if self.right_node is not None:
                rn = self.right_node.printLevel(depth - 1)
        elif depth == 0:
            return [self.key]
        return ln + rn


    def __str__(self):
        return self._str_preorder()

    def _str_preorder(self, level=0):
        tree = ""
        if self.key is not None:
            tree += str(self.key).center(3)
            if self.left_node is not None:
                tree += "\n | \n *" + " " * level + "--*" + self.left_node._str_preorder(level + 1)
            if self.right_node is not None:
                tree += "\n | \n *" + " " * level + "-- *" + self.right_node._str_preorder(level + 1)
        return tree

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
    bt.bst_insert_rek(11)
    bt.bst_insert_rek(29)
    bt.bst_insert_rek(38)
    bt.bst_insert_rek(39)
    bt.bst_insert_rek(40)
    bt.bst_insert_rek(41)
    bt.bst_insert_rek(42)
    return bt


def test_weight():
    bt = __setup_tree()
    assert bt.weight() == 12


def test_height():
    bt = __setup_tree()
    assert bt.height() == 7


def test_is_key():
    bt = __setup_tree()
    assert bt.is_key(42)


def test_depth():
    bt = __setup_tree()
    assert bt.depth(42) == 7

def test_printLevel():
    bt = __setup_tree()
    bt.printLevel(2) == [2, 11, 35]
