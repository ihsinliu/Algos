class Solution:
    """
    @param s: A list of integers
    @return: An integer
    """
    def triangle_count(self, s: List[int]) -> int:
        # write your code here
        nums = sorted(s)
        res = 0
        for i in range(len(nums)):        
            left = 0
            right = i - 1
            target = nums[i]
            while left < right:
                if nums[left] + nums[right] > target:
                    res+= right - left
                    right-=1
                else:
                    left+=1

        return res
