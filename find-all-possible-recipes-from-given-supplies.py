class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegree = {r: 0 for r in recipes}  # Store number of dependencies
        graph = defaultdict(list)  # Store ingredient-to-recipe mappings
        supply_set = set(supplies)  # Quick lookup for available ingredients
    
        for r, ing_list in zip(recipes, ingredients):
            for ing in ing_list:
                if ing not in supply_set:  # If ingredient is not a direct supply
                    graph[ing].append(r)  # This ingredient is required for recipe r
                    indegree[r] += 1  # Increase dependency count
    
        queue = deque([r for r in recipes if indegree[r] == 0])
        result = []

        while queue:
            r = queue.popleft()
            result.append(r)  # Recipe can be made
        
            for dependent_recipe in graph[r]:
                indegree[dependent_recipe] -= 1
                if indegree[dependent_recipe] == 0:  # All ingredients available
                    queue.append(dependent_recipe)

        return result
