class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reversed_graph = defaultdict(list)
        outdegree = [0] * n        
        for node, neighbors in enumerate(graph):
            outdegree[node] = len(neighbors)
            for neighbor in neighbors:
                reversed_graph[neighbor].append(node)
        queue = deque([i for i in range(n) if outdegree[i] == 0])
        safe_nodes = set(queue)        
        while queue:
            node = queue.popleft()
            for neighbor in reversed_graph[node]:
                outdegree[neighbor] -= 1
                if outdegree[neighbor] == 0:
                    safe_nodes.add(neighbor)
                    queue.append(neighbor)
        return sorted(safe_nodes)
