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

        res = ""
        while l <= r:
            m = (l+r)//2

            if values[m][0] <= timestamp:
                res = values[m][1]
                l = m+1
            else:
                r = m-1
        return res



            

        
