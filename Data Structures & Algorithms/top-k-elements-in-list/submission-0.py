class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_Map = {}
        res=[]
        j=0
        for i in nums:
            if i in hash_Map:
                hash_Map[i] += 1
            else:
                hash_Map[i] = 1

        while j < k:
            maxKey = max(hash_Map, key = hash_Map.get)
            res.append(maxKey)
            hash_Map.pop(maxKey)
            j+=1
        return res