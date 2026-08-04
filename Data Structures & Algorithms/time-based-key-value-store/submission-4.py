class TimeMap:
    from collections import defaultdict
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res, nums = "", self.store.get(key, [])
        
        l,r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid][0] <= timestamp:
                res = nums[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res
