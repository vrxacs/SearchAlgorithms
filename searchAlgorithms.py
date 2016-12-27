from collections import deque
import heapq

class PriorityQueue():
    def __init__(self):
        self.queue = []
        self.current = 0

    def next(self):
        if self.current >= len(self.queue):
            raise StopIteration

        out = self.queue[self.current]
        self.current += 1

        return out

    def peek(self):
        return self.queue[0]

    def pop(self):
        return heapq.heappop(self.queue)

    def __iter__(self):
        return self

    def __str__(self):
        return 'PQ:[%s]' % (', '.join([str(i) for i in self.queue]))

    def append(self, node):
        heapq.heappush(self.queue, node)

    def extend(self, nodes):
        for n in nodes:
            self.append(n)

    def size(self):
        s = 0
        for n in self.queue:
            s += 1
        return s

    def __contains__(self, key):
        self.current = 0
        return key in [n for v, n in self.queue]

    def __eq__(self, other):
        self.current = 0
        return self == other

    __next__ = next

def breadth_first_search(graph, start, goal):
    class Node:
        def __init__(self, n, p):
            self.node = n
            self.parent = p
    def solution(node):
        path = []
        path.append(node.node)
        next = node.parent
        while next is not None:
            path.append(next.node)
            next = next.parent
        return path[::-1]
    if start == goal:
        return []
    frontier = deque([])
    startNode = Node(start, None)
    nextNodes = graph[start]
    # TODO: maybe refactor this to include it in the loop below
    if goal in nextNodes:
        return solution(Node(goal, startNode))
    expandedNodes = [Node(n, startNode) for n in nextNodes]
    frontier.extend(expandedNodes)
    explored = []
    explored.append(startNode)
    while True:
        if len(frontier) == 0:
            print "Error! Empty frontier"
            return []
        node = frontier.popleft()
        explored.append(node)
        nextNodes = graph[node.node]
        if goal in nextNodes:
            return solution(Node(goal, node))
        expandedNodes = [Node(n, node) for n in nextNodes if n not in frontier and n not in explored]

        frontier.extend(expandedNodes)
