class Solution:
    def maximumInvitations(self, favorite: list[int]) -> int:
        n = len(favorite)

        # Step 1: Identify all cycles
        visited = [-1] * n
        stack_index = [-1] * n
        cycle_sizes = []
        node_in_cycle = [-1] * n  # -1 means not in a cycle

        def find_cycles(node):
            stack = []
            while visited[node] == -1:
                visited[node] = 1  # Mark as visiting
                stack.append(node)
                stack_index[node] = len(stack) - 1
                node = favorite[node]

            if stack_index[node] != -1:  # Cycle detected
                cycle_len = len(stack) - stack_index[node]
                cycle_sizes.append(cycle_len)
                for i in range(stack_index[node], len(stack)):
                    node_in_cycle[stack[i]] = 1  # Mark nodes as part of a cycle

            # Reset stack indices for visited nodes
            for i in stack:
                stack_index[i] = -1

        for i in range(n):
            if visited[i] == -1:
                find_cycles(i)

        # Step 2: Calculate chain lengths
        longest_chain = [0] * n
        indegree = [0] * n

        for i in range(n):
            indegree[favorite[i]] += 1

        queue = deque(i for i in range(n) if indegree[i] == 0)

        while queue:
            node = queue.popleft()
            next_node = favorite[node]
            longest_chain[next_node] = max(longest_chain[next_node], longest_chain[node] + 1)
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                queue.append(next_node)

        # Step 3: Handle 2-cycles and compute result
        two_cycle_contribution = 0
        visited_two_cycles = set()

        for i in range(n):
            if favorite[favorite[i]] == i and i not in visited_two_cycles:
                visited_two_cycles.add(i)
                visited_two_cycles.add(favorite[i])
                two_cycle_contribution += 2 + longest_chain[i] + longest_chain[favorite[i]]

        # Step 4: Calculate maximum invitations
        max_cycle = max(cycle_sizes) if cycle_sizes else 0
        return max(max_cycle, two_cycle_contribution)
