class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        pre = [0] * len(height)
        post = [0] * len(height)

        for i in range(1, len(pre)):
            pre[i] = max(pre[i - 1], height[i - 1])

        for i in range(len(post) - 2, -1 , - 1):
            post[i] = max(post[i + 1], height[i + 1])

        for i, h in enumerate(height):
            diff = max(min(pre[i], post[i]) - h, 0)
            total += diff

        return total 

