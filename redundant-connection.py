class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n 
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False  
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1        
        return True

class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)
        uf = UnionFind(n + 1)  
        for u, v in edges:
            if not uf.union(u, v):
                return [u, v]  
