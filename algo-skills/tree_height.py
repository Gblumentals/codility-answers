# longest path / tree height binary tree
from extratypes import Tree  # library with types used in the task

def longest_path(root):
    # If root is null means there
    # is no binary tree so
    # return a empty vector

    if root == None:
        return []

    # Recursive call on root.right
    rightvect = longest_path(root.r)

    # Recursive call on root.left
    leftvect = longest_path(root.l)

    # Compare the size of the two vectors
    # and insert current node accordingly
    if (len(leftvect) > len(rightvect)):
        leftvect.append(root.x)
    else:
        rightvect.append(root.x)

    # Return the appropriate vector
    if len(leftvect) > len(rightvect):
        return leftvect

    return rightvect
    return ''


def solution(T):
    if T == None:
        return -1

    n = len(longest_path(T))

    return n - 1
