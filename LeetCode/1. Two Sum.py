class Solution:
    def twoSum_two_pointers(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        nums = [(num, index) for index, num in enumerate(nums)]
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left][0] + nums[right][0]  > target:
                right-=1
            elif nums[left][0]  + nums[right][0]  < target:
                left +=1
            else:
                return sorted([nums[left][1], nums[right][1]])
        
        return [-1, -1]
    
    def twoSum_hash(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i in range(len(nums)):
            num = nums[i]
            if target - num in res:
                return [i, res[target - num]]
            res[num] = i
        
        return [-1, -1]
