class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counts = Counter(answers)
        total_rabbits = 0
        
        for answer, frequency in counts.items():
            group_size = answer + 1  # Size of each color group
            # Calculate number of complete groups needed
            num_groups = (frequency + group_size - 1) // group_size
            # Add all rabbits from complete groups
            total_rabbits += num_groups * group_size
            
        return total_rabbits
