class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sortedList = sorted(set(nums)) 
        count = 1
        max_count = 1

        for i in range(1, len(sortedList)):
            if sortedList[i] == sortedList[i - 1] + 1:
                count += 1
            else:
                count = 1  
            max_count = max(max_count, count)

        return max_count
