edges = {}
n = int(input())
for _ in range(n):
    dad, left, right = input().split()
    if left == ".": left = None
    if right == ".": right = None
    edges[dad] = (left, right)


def preorder(root):
    print(root, end="")
    if edges[root][0]:
        preorder(edges[root][0])
    if edges[root][1]:
        preorder(edges[root][1])


def postorder(root):
    if edges[root][0]:
        postorder(edges[root][0])
    if edges[root][1]:
        postorder(edges[root][1])
    print(root, end="")



def inorder(root):
    if edges[root][0]:
        inorder(edges[root][0])
    print(root, end="")
    if edges[root][1]:
        inorder(edges[root][1])

preorder("A")
print()
inorder("A")
print()
postorder("A")
