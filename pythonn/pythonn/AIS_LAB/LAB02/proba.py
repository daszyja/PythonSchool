class insertion(object):
    """docstring for ClassName"""

    def __init__(self, size, ch):
        self.size = size
        self.ch = ch
        self.data = []
        for i in range(size):
            self.data.append(input("Enter number into list:"))
        if(ch == 1):
            self.ascsorting()
        else:
            self.dscsorting()

    def ascsorting(self):
        for i in range(1, self.size):
            j = i
            while j > 0 and int(self.data[j - 1]) > int(self.data[j]):
                self.data[j - 1], self.data[j] = self.data[j], self.data[j - 1]
                j = j - 1
        print ("\nSorted Data is: " + str(self.data))

    def dscsorting(self):
        for i in range(1, self.size):
            j = i
            while j > 0 and int(self.data[j - 1]) < int(self.data[j]):
                self.data[j - 1], self.data[j] = self.data[j], self.data[j - 1]
                j = j - 1
        print ("\nSorted Data is " + str(self.data))

ch = int(input(
    "Enter choice according to order of sort 1.ascending order 2. Descending order: "))
size = int(input("Enter size of the list: "))
a = insertion(size, ch)
