class Solution:
    def trap_reverse(self, i, j, height):
        x = j
        y = j - 1
        water = 0
        # keep going while we have more towers
        while x >= i:
            # keep going as long as were not in the end and the next tower is smaller then the first
            while y >= i and height[x] > height[y]:
                y -= 1
            # add the water from inside the block
            water_level = min(height[x], height[y])
            k = y + 1
            while k < x:
                water += water_level - height[k]
                k += 1
            x = y
            y -= 1
        return water
    def trap(self, height: List[int]) -> int:
        i = 0
        j = 1
        water = 0
        n = len(height)
        # keep going while we have more towers
        while i < len(height):
            # keep going as long as were not in the end and the next tower is smaller then the first
            while j < n and height[i] > height[j]:
                j += 1
            # if we reached the end and didnt find a bigger tower then the start we trap from reverse and end
            if j >= n:
                water += self.trap_reverse(i, j - 1, height)
                break
            # add the water from inside the block
            water_level = min(height[i], height[j])
            k = i + 1
            while k < j:
                water += water_level - height[k]
                k += 1
            i = j
            j += 1
        return water