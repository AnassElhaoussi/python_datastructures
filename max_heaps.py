# MaxHeap : Complete Binary tree - Every node should be lower than its parent
# MaxHeap is FAST : You can insert in O(log n), you can get max in O(1) and you can remove max in O(log n)
# MaxHeaps operations : Push(insert) Peek(get_max) pop(remove_max)


class MaxHeap:
    def _init__(self, items=[]):
        super().__init__()
        self.heap = [0]

        for item in items:
            self.heap.append(item)
            self.__floatUp((len(self.heap) - 1))

    def push(self, data):  # Here we have our push operation that appends the item to the end of the Heap and then float it up until it becomes lower than its parent
        self.heap.append(data)
        self.__floatUp(len(self.heap)-1)

    def peek(self):  # Here's our peek operartion that print out the max item of the Heap
        if self.heap[1]:
            return self.heap[1]

        else:
            return False

    def pop(self):  # Pop operation that pops the max item by swapping it with the last item in our MaxHeap and then bubble it down recursively until the parent becomes greather than its child
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)

        elif len(self.heap) == 2:
            max = self.heap.pop()

        else:
            max = False
        return max

    def __swap(self, i, j):
        # Swapping two items by changing their positions
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index // 2
        if index <= 1:
            return

        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index

        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left

        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right

        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)

    def __str__(self):
        str(self.heap)
