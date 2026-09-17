class Solution:
    def merge(self, nums, left, mid, right):
        left_arr = nums[left : mid + 1]
        right_arr = nums[mid + 1 : right + 1]
        p1 = 0
        p2 = 0
        k = left

        while p1 < len(left_arr) and p2 < len(right_arr):
            if left_arr[p1] < right_arr[p2]:
                nums[k] = left_arr[p1]
                p1 += 1
            else:
                nums[k] = right_arr[p2]
                p2 += 1
            k += 1
        
        while p1 < len(left_arr):
            nums[k] = left_arr[p1]
            k += 1
            p1 += 1

        while p2 < len(right_arr):
            nums[k] = right_arr[p2]
            k += 1
            p2 += 1


    def mergeSort(self, nums, left, right):
        # base case
        if left < right:
            mid = (left + right) // 2
            self.mergeSort(nums, left, mid)
            self.mergeSort(nums, mid + 1, right)
            self.merge(nums, left, mid, right)
        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums, 0, len(nums) - 1)

        # merge sort

#         # bucket list
#         # index refers to the ele in the list
#         # create the size of list of a max ele
#         # all ele in the list currently 0
        
#         # iterate thru the nums
#         #   increment the freq count in the curr ele index
        
#         # iterate thru the new created list
#         #   if the curr ele is not 0 
#         #       add the ele to the res list
#         # O(n) and O(k) where k is the largest ele in the arr

#         max_ele = max(nums)
#         temp_lst = [0] * (max_ele + 1)
#         res = []

#         for i in range(len(nums)):
#             temp_lst[nums[i]] += 1

#         print(temp_lst)
#         for i in range(len(temp_lst)):
#             if temp_lst[i] != 0:
#                 for j in range(temp_lst[i]):
#                     res.append(i)

#         return res


        

