class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
             we will sort your return value in output
    """
    def fourSum(self, numbers, target):
        if not numbers:
            return []
            
        nums = sorted(numbers)
        results = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                pairs = self.find_two_sum_pairs(
                    nums,
                    j + 1,
                    len(nums) - 1,
                    target - nums[i] - nums[j],
                )
                
                for (c, d) in pairs:
                    results.append([nums[i], nums[j], c, d])
                
        return results
        
    def find_two_sum_pairs(self, nums, left, right, target):
        res = []
        last_pair = None
        while(left<right):
            if nums[left] + nums[right] == target:
                if not last_pair or last_pair != (nums[left], nums[right]):
                    res.append((nums[left], nums[right]))
                last_pair = (nums[left], nums[right])
                left+=1
                right-=1
            elif nums[left] + nums[right] < target:
                left+=1
            else:
                right-=1

        return res