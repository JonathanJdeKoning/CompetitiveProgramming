def _parent(x):
    return x // 2
def _left(x):
    return 2*x
def _right(x):
    return 2*x + 1

class SumSegmentTree:
    def __init__(self, A):
        """Create the segment tree for array A. Complexity: O(n)."""
        self.size = len(A)
        self._N = 2 ** (self.size - 1).bit_length() #_N is size rounded up to the closest power of 2.
        self._T = [0] * 2*self._N
        self._first_leaf = self._N
    
        for i in range(self.size):
            self._T[self._first_leaf + i] = A[i]
        
        for node in range(self._first_leaf - 1, 1, -1):
            self._fixElement(node)
    
    #Computes the value of an internal node from the children
    def _fixElement(self, node):
        self._T[node] = self._T[_left(node)] + self._T[_right(node)]
    
    #Computes the value of each internal node, from the given one up to the root.
    def _fixUp(self, node):
        while node >= 1:
            self._fixElement(node)
            node = _parent(node)
    
    def get(self, i):
        """Returns the element at index i. Complexity: O(1)"""
        return self._T[self._first_leaf + i]

    def set(self, i, x):
        """Set the element at index i to x. Complexity: O(log n)"""
        self._T[self._first_leaf + i] = x
        self._fixUp(_parent(self._first_leaf + i))

    def get_data(self):
        """Returns a list of the values stored in the array"""
        return self._T[self._first_leaf:self._first_leaf + self.size]
    
    def _sum(self, i, j, node, node_begin, node_end):
        if j < node_begin or i > node_end:
            return 0 #node's interval completely out of query interval
        elif i <= node_begin and node_end <= j:
            return self._T[node] #node's interval completely contained in query interval
        else:
            node_size = node_end - node_begin + 1
            return self._sum(i, j,  _left(node), node_begin, node_end - node_size / 2) +\
                   self._sum(i, j, _right(node), node_begin + node_size / 2, node_end)
    
    def sum(self, i, j):
        """Returns the sum of all the elements from index i to index j (inclusive). Complexity: O(log n)"""
        return self._sum(i, j, 1, 0, self._N - 1)   
numElems, numUpdates, numQueries= list(map(int, input().split()))
nums = [int(input()) for _ in range(numElems)]

segTree = SumSegmentTree(nums)
for _ in range(numUpdates+numQueries):
    a,b,c = list(map(int, input().split()))
    if a == 1:
        segTree.set(b-1, c)
    else:
        print(segTree.sum(b-1,c-1))

