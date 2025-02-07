class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_map = {}  # Maps ball index to color
        unique_colors = set()  # Stores unique colors
        color_count = {}  # Counts occurrences of each color
        result = []
        
        for x, y in queries:
            prev_color = color_map.get(x, None)  # Get previous color of ball x
            
            if prev_color is not None:
                # Decrease count of previous color
                color_count[prev_color] -= 1
                if color_count[prev_color] == 0:
                    unique_colors.discard(prev_color)  # Remove if no balls have it
            
            # Assign new color
            color_map[x] = y
            color_count[y] = color_count.get(y, 0) + 1
            unique_colors.add(y)  # Ensure the color is in the set
            
            # Store result
            result.append(len(unique_colors))
        
        return result
