class Solution:
    """
    @param a: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def k_closest_numbers(self, a: List[int], target: int, k: int) -> List[int]:
        if not a or k<=0:
            return []
        l = 0
        r = len(a) - 1
        target_index = -1
        res = []
        # binary search for target
        while l + 1 < r:
            mid = (l+r)//2
            val = a[mid]
            if val < target:
                l = mid
            else:
                r = mid
            
        # if target found, set target_index
        if a[l] == target:
            target_index = l
        elif a[r] == target:
            target_index = r
        # set left and right pointer. If target found, add it to res as well
        if target_index == -1:
            lp = l
            rp = r
        else:
            res.append(target)
            lp = target_index-1
            rp = target_index+1
        
        #move lp and rp until res reaches required length
        while len(res)<k:
            if self.distance(a, lp, target) <= self.distance(a, rp, target):
                res.append(a[lp])
                lp-=1
            else :
                res.append(a[rp])
                rp+=1

        return res

    def distance(self, a:List[int], x: int, target: int):
        if x < 0 or x >= len(a):
            return sys.maxsize
        return a[x]-target if a[x]-target>0 else target-a[x]