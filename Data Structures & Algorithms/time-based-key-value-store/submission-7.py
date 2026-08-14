class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        if (key, timestamp) in self.time_map:
            return self.time_map[(key, timestamp)]
        else:
            temp_time = timestamp
            while temp_time > 0:
                temp_time -= 1
                if (key, temp_time) in self.time_map:
                    return self.time_map[(key, temp_time)]
            return ""

