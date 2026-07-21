from collections import deque

class FlowNetwork:
    def __init__(self):
        self.graph ={}
        self.capacity = {}
    def add_edge(self, start, end, capacity):
        if start not in self.graph:
            self.graph[start] = []

        if end not in self.graph:
            self.graph[end] = []

        self.graph[start].append(end)
        self.graph[end].append(start)

        self.capacity[(start, end)] = capacity
        self.capacity[(end, start)] = 0

    def bfs(self, source, sink, parent, flow):
        visited = {source}
        queue = deque([source])

        while queue:
            current = queue.popleft()
             
            for neighbour in self.graph[current]:
                residual_capacity =(
                    self.capacity[(current, neighbour)]
                    - flow[(current, neighbour)]
                )
                if neighbour not in visited and residual_capacity > 0:
                    visited.add(neighbour)
                    parent[neighbour] = current
                    queue.append(neighbour)
                    if neighbour == sink:
                        return True
        return False
    def edmonds_karp(self, source, sink):
        flow ={}

        for edge in self.capacity:
            flow[edge] = 0
        max_flow = 0
        iteration = 1
        steps = []

        while True:
            parent = {}

            if not self.bfs(source, sink, parent, flow):
                break

            path_flow = float("inf")
            current = sink
            path = []
            while current != source:
                previous = parent[current]
                path_flow = min(
                    path_flow,
                    self.capacity[(previous, current)]
                    - flow[(previous, current)]
                )
                path.append((previous, current))
                current = previous
            path.reverse()
    
            for start, end in path:
                flow[(start, end)] += path_flow
                flow[(end, start)] -= path_flow

            max_flow += path_flow
            steps.append((iteration, path, path_flow, max_flow))
            iteration +=1
    
        return max_flow, flow, steps
