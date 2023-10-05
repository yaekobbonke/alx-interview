#!/usr/bin/python3
''' Lockboxes'''


def canUnlockAll(boxes):
    '''if all the boxes can be opened'''
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
