class TimeMap:

    def __init__(self):
        # hashmap
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = [(value, timestamp)]
        else:
            self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:

        most_recent = ''
        if key not in self.map:
            return most_recent
        
        l = 0
        r = len(self.map[key]) - 1

        while l <= r:
            mid = (l + r) // 2

            if self.map[key][mid][1] == timestamp:
                return self.map[key][mid][0]

            elif self.map[key][mid][1] < timestamp:
                most_recent = self.map[key][mid][0]
                l = mid + 1 # there may be more recent timestamps on the right side before timestamp
                
            else:
                r = mid - 1
                

        return most_recent
                
        
