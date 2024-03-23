n = int(input())
tree = []
for _ in range(n):
    tree.append(input().split())
tree.sort(key=lambda x:x[0])

def preorder(v):
    if v != '.':
        root, left, right = tree[ord(v)-65]
        print(root, end='')
        preorder(left)
        preorder(right)
def inorder(v):
    if v != '.':
        root, left, right = tree[ord(v)-65]
        inorder(left)
        print(root, end='')
        inorder(right)
def postorder(v):
    if v != '.':
        root, left, right = tree[ord(v)-65]
        postorder(left)
        postorder(right)
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')