import sys

input = sys.stdin.readline

N = int(input())
tree = {}

for n in range(N):
    root, left, right = map(str, input().split())
    tree[root] = [left, right]


def first(root):
    if root != '.':
        print(root, end='')
        first(tree[root][0])
        first(tree[root][1])


def mid(root):
    if root != '.':
        mid(tree[root][0])
        print(root, end='')
        mid(tree[root][1])


def end(root):
    if root != '.':
        end(tree[root][0])
        end(tree[root][1])
        print(root, end='')


root = 'A'

first(root)
print()
mid(root)
print()
end(root)
