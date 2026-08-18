class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        a = nums1
        b = nums2
        if len(nums2) < len(nums1): # a is smaller array
            a = nums2
            b = nums1
        l, r = 0, len(a) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2
            Aleft = a[i] if i >= 0 else float("-infinity")
            Aright = a[i + 1] if (i + 1) < len(a) else float("infinity")
            Bleft = b[j] if j >= 0 else float("-infinity")
            Bright = b[j + 1] if (j + 1) < len(b) else float("infinity")
            if Aleft > Bright:
                r = i - 1
            elif Bleft > Aright:
                l = i + 1
            else: # found proper partition
                if total % 2 == 0: # even number of elements
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return float(min(Aright, Bright))
                

            

               
            



                
