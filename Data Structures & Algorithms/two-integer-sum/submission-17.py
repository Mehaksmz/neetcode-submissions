class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        l = 0
        r = len(nums) - 1
        
        for (idx, val) in enumerate(nums):
            arr.append((val, idx))
        arr.sort()

        while l < r:
            sum = arr[l][0] + arr[r][0]
            if sum == target:
                break
            elif sum < target:
                l += 1
            else:
                r -= 1      
        result = [arr[l][1], arr[r][1]]
        result.sort()
        return result