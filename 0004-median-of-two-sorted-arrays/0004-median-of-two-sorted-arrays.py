class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        x=sorted(nums1+nums2)
        y = len(x)
        if(y%2==1):
            return float(x[y//2])
        else:
            return float(x[y//2-1]+x[y//2])/2