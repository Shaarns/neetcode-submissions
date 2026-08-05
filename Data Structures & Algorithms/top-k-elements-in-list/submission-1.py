class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        obj = {}
        res = []
        for num in nums:
            obj[num] = obj.get(num, 0) + 1
        
        for i in range(k):
            max_freq = 0
            elem = None
            for key, value in obj.items():
                if max_freq < value:
                    max_freq = value
                    elem = key

            res.append(elem)
            obj.pop(elem)
        return res
                


