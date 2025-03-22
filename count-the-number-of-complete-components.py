class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)

        # Build the adjacency list
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        # These should be outside the loop!
        visited = set()
        complete_components = 0

        def dfs(node, component):
            stack = [node]
            while stack:
                curr = stack.pop()
                if curr not in visited:
                    visited.add(curr)
                    component.add(curr)
                    stack.extend(graph[curr] - visited)

        # Find and check each connected component
        for node in range(n):
            if node not in visited:
                component = set()
                dfs(node, component)
                
                # A complete component of k nodes should have exactly k*(k-1)/2 edges
                edge_count = sum(len(graph[v]) for v in component) // 2
                if edge_count == len(component) * (len(component) - 1) // 2:
                    complete_components += 1

        return complete_components
