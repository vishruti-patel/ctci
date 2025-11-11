from collections import deque

graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}


def dfs_graph(start_node, graph):
    visited = set()
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end = " ")


            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
    print()

dfs_graph('A', graph)



def bfs_graph(start_node, graph):
    visited = set()
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(node, end= " ")

            for neigh in graph[node]:
                if neigh not in visited:
                    queue.append(neigh)

    print()

bfs_graph('A', graph)


def add_node(graph, node):
    if node not in graph:
        graph[node] = []

    print()


def add_edge_undirected(graph, node1, node2):
    #for undirected graph:
    if node1 not in graph:
        add_node(graph, node1)
    if node2 not in graph:
        add_node(graph, node2)
    graph[node1].append(node2)
    graph[node2].append(node1)
    #for directed:

def add_edge_directed(graph, src, target):
    if src not in graph:
        add_node(graph, src)
    if target not in graph:
        add_node(graph, target)
    graph[src].append(target)



def remove_node(graph, node):
    if node in graph:
        for neigh in list(graph[node]):
            graph[neigh].remove(node)
        del graph[node]

def remove_edge(graph, node1, node2):
    if node1 in graph and node2 in graph[node1]:
        graph[node1].remove(node2)
    if node2 in graph and node1 in graph[node2]:
        graph[node2].remove(node1)
    pass








