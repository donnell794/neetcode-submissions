class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        arr = self.store.get(key,[])
        left, right = 0, len(arr)-1

        while left <= right:
            mid = (left + right) // 2
            t = arr[mid][0]
            if t == timestamp:
                return arr[mid][1]
            if t < timestamp:
                left = mid + 1
                res = arr[mid][1]
            else:
                right = mid - 1

        return res
