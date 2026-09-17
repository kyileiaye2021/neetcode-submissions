class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # two pointer
        # first 
        # second
        # until num1 and nums2 is not empty
        #   check if first ele > second
        #       add the second ele to the new arr
        #   else
        #       add the first ele to the new arr
        # check if the len is odd
        #   l,r  = 0, 1
        #   find mid index and return mid ele
        # else
        #   n = new arr len
        #   l, r = 0, n - 2
        #   find mid1 index and get mid1 ele
        #   l = 1, r = n - 1
        #   find the mid2 index and get mid2 ele
        #   combine mid1 and mid2 ele and get the medium
        # return median

        first, second =0, 0
        new_arr= []
        while first < len(nums1) and second < len(nums2):
            if nums1[first] > nums2[second]:
                new_arr.append(nums2[second])
                second += 1
            else:
                new_arr.append(nums1[first])
                first += 1

        while first < len(nums1):
            new_arr.append(nums1[first])
            first += 1

        while second < len(nums2):
            new_arr.append(nums2[second])
            second += 1

        n = len(new_arr)

        if n % 2 != 0: # odd len
            l, r = 0, n - 1
            mid = (l + r) // 2
            return new_arr[mid]

        else:
            if n >= 2:
                l, r = 0, n - 2 
                mid = (l+r)//2
                medium1 = new_arr[mid]

                l, r = 1, n - 1
                mid = (l + r) // 2
                medium2 = new_arr[mid]
                return (medium1 + medium2) / 2

        return float('nan')



