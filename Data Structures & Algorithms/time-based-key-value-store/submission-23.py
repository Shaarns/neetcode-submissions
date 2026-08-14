class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[(key)].append((timestamp, value))
        else:
            self.time_map[(key)] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""

        values = self.time_map[key]

        l = 0
        r = len(values) - 1
        #[2, 4, 5, 7, 9, 12, 23, 45, 56] [1, 2, 3, 4]
        res = ""
        while l <= r:
            m = (l+r)//2

            if values[m][0] <= timestamp:
                # print(values[m][1])
                res = values[m][1]

            if timestamp < values[m][0]:
                r = m-1
            else:
                l = m+1
        return res



            

        
