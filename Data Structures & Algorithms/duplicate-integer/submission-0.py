class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         # set container
         # iterate over the list
         #      check if the curr ele is in the visited set
         #          return false
         #      add the curr ele in the set container
         # return True

        visited = set()

        for ele in nums:
            if ele in visited:
                return True
            else:
                visited.add(ele)
        return False
