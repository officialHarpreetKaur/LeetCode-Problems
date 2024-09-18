class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Initialize the maximum reachable index
        max_reach = 0

        # Iterate through the array
        for i, jump in enumerate(nums):
            # If the current index cannot be reached, return False
            if i > max_reach:
                return False

            # Update the maximum reachable index
            max_reach = max(max_reach, i + jump)

        # If the last index can be reached, return True
        return max_reach >= len(nums) - 1