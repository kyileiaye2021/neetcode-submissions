class TimeMap:

    def __init__(self):
        self.key_val_map = defaultdict(list) # {string : stack}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_val_map[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res = ''
        if key in self.key_val_map:

            l, r = 0, len(self.key_val_map[key]) - 1

            while l <= r:
                mid = (l + r)// 2
                if timestamp > self.key_val_map[key][mid][1]:
                    res = self.key_val_map[key][mid][0]
                    l = mid + 1
                elif timestamp < self.key_val_map[key][mid][1]:
                    r = mid - 1
                else:
                    return self.key_val_map[key][mid][0]

            return res
        else:
            return ""


        
