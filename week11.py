from collections import deque

graph = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0]
]

def dfs(g, i, visited):
    visited[i] = 1
    print(chr(ord('A')+i),end=' ')
    for j in range(len(g)):
        if g[i][j] == 1 and not visited[j]:
            dfs(g, j, visited)

def bfs(g, i, visited): # 제규를 사용하지 않음
    queue = deque()
    visited[i] = 1
    queue.append(i)

    while queue:
        v = queue.popleft()
        print(chr(ord('A') + v), end=' ')
        for j in range(len(g)):
            if g[v][j] == 1 and not visited[j]:
                visited[j] = 1
                queue.append(j)

visited_dfs = [0 for _ in range(len(graph))]
visited_bfs = [0 for _ in range(len(graph))]
dfs(graph,0, visited_dfs)
print()
bfs(graph, 0, visited_bfs)