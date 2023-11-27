class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        i = 1
        while (True):
            val = reader.get(i-1)
            if val >= target:
                break
            
            i *= 2
        
        l = 0
        r = i - 1
        while l + 1 < r:
            mid = (l+r)//2
            val = reader.get(mid)
            if val < target:
                l = mid
            else:
                r = mid
            
        if reader.get(l) ==target:
            return l
        if reader.get(r)==target:
            return r
        
        return -1