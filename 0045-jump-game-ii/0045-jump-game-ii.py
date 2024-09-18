class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        current_jump_end = 0
        max_reach = 0

        for i in range(n - 1):
            max_reach = max(max_reach, i + nums[i])
            if i == current_jump_end:
                jumps += 1
                current_jump_end = max_reach

        return jumps