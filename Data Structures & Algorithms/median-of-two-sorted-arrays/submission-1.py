class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # happy casees
        # nums1= [1], nums2= [2]
        # output = 1.5

        # nums1= [5], nums2= [5,5]
        # output = [5]

        # edge cases
        # nums1= [], nums2=[5]
        # output: [5]

        # nums1 = [5,6], nums2 = []
        # 5.5

        # total = len(nums1) + len(nums2)
        # half = total // 2

        # find binary search on smaller arr
        # smaller arr = nums1 if len(nums1) < len(nums2) else nums2

        # l = 0
        # r = len(smaller arr) - 1
        # smaller_last idx = 0
        #larger_last_idx = 0
        # while true
        #   mid = (l + r) // 2
        #   smaller_last idx = mid
        #   larger_last_idx = half - mid
        #   if mid ele < larger last idx + 1 ele and larger_last_idx ele < mid + 1 ele
            # if total % 2 == 0:
            #   max(smaller_last_idx, larger_last_idx) + min(smaller_last_idx + 1, larger_last_idx + 1) / 2
            # else:
            #   min(smaller_last_idx + 1, larger_last_idx + 1)
            
        #   elif mid ele > larger last idx + 1 ele 
        #       l = mid + 1
        #   else
        #       r = mid - 1

        total = len(nums1) + len(nums2)
        half = total // 2
        if len(nums1) <= len(nums2):
            smaller = nums1
            larger = nums2
        else:
            smaller = nums2
            larger = nums1
            
        l = 0
        r = len(smaller) - 1
        
        while True:
            i = (l + r) // 2
            j = half - i - 2

            smaller_left = smaller[i] if i >= 0 else float('-inf')
            smaller_right = smaller[i + 1] if i + 1 < len(smaller) else float('inf')
            larger_left = larger[j] if j >= 0 else float('-inf')
            larger_right = larger[j + 1] if j + 1 < len(larger) else float('inf')
            
            if smaller_left <= larger_right and larger_left <= smaller_right: 
                
                if total % 2 == 0:
                    return (max(smaller_left, larger_left) + min(smaller_right, larger_right)) / 2
                else:
                    return min(smaller_right, larger_right)

            elif smaller_left > larger_right:
                r = i - 1

            else:
                l = i + 1


    