class Solution:
    """
    @param a: a list
    @param b: a list
    @param c: a list
    @param d: a list
    @return: how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero
    """
    def four_sum_count(self, a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
        # Write your code here
        aB = {}
        res = 0
        for i in range(len(a)):
            for j in range(len(b)):
                num = a[i]+b[j]
                if num not in aB:
                    aB[num] = 1
                else:
                    aB[num]+=1
        
        for i in range(len(c)):
            for j in range(len(d)):
                val= -c[i]-d[j]
                if val in aB:
                    res+=aB[val]

        return res