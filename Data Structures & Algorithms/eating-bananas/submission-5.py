class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        min_rate = float('inf')
        l = 1
        r = max(piles)

        while l <= r:
            m = (l+r)//2
            total_hours = 0

            for banana in piles:
                total_hours += math.ceil(banana/m)

            if total_hours <= h:
                min_rate = min(min_rate, m)
                r = m - 1
            else:
                l = m+1

        print(min_rate)
        return int(min_rate)

                


#     print('banana', banana)
            #     print('rate', rate)
            #     # print("remainder",remainder)
            #     print('total hours', total_hours)
            # print('*********************')