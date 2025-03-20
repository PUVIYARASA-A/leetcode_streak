class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.weight = [(1 << 17) - 1] * n  # Initialize with all bits set

    def find(self, u: int) -> int:
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u: int, v: int, w: int):
        root_u = self.find(u)
        root_v = self.find(v)
        new_weight = self.weight[root_u] & self.weight[root_v] & w
        self.weight[root_u] = new_weight
        self.weight[root_v] = new_weight
        
        if root_u == root_v:
            return
        
        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

    def get_min_cost(self, u: int, v: int) -> int:
        if self.find(u) == self.find(v):
            return self.weight[self.find(u)]
        return -1

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        uf = UnionFind(n)
        
        for u, v, w in edges:
            uf.union(u, v, w)
        
        result = []
        for s, t in queries:
            result.append(0 if s == t else uf.get_min_cost(s, t))
        
        return result
