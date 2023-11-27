class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        self.sortColors(colors, 0, k, 0, len(colors)-1)

    def sortColors(self, colors, colors_from, colors_to, index_from, index_to):
        if colors_from == colors_to or index_from == index_to:
            return
        
        l = index_from
        r = index_to
        color = (colors_from + colors_to) //2
        while l<=r:
            while l<=r and colors[l] <= color:
                l+=1
            while l<=r and colors[r] > color:
                r-=1
            
            if l<=r:
                colors[l], colors[r] = colors[r], colors[l]
                l+=1
                r-=1
        
        self.sortColors(colors, colors_from, color, index_from, r)
        self.sortColors(colors, color+1, colors_to, l, index_to)