class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # hashmap
        unique = collections.defaultdict(int)
        res = []

        for n in nums:
            unique[n] = unique.get(n, 0) + 1

        print(unique)
        for key, val in unique.items():
            if val > (len(nums) // 3):
                res.append(key)

        return res

        
