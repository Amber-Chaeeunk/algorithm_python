class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.dfs(nums, result, [])
        return result
    
    def dfs(self, nums, result, path):
        if not nums and path not in result:
            result.append(path)
        else:
            for i in range(len(nums)):
                self.dfs(nums[:i] + nums[i + 1:], result, path + [nums[i]])
