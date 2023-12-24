N, tree_len = map(int, input().split())
trees = list(map(int, input().split()))

left, right = 0, max(trees)

while left <= right:
    mid = (left + right) // 2
    tree_get = 0
    for i in trees:
        if i >= mid:
            tree_get += i - mid

    if tree_get >= tree_len:
        left = mid + 1
    else:
        right = mid - 1

print(right)
