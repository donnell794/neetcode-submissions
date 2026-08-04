class Solution:
    import heapq
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        freq_dict = {}
        for task in tasks:
            freq_dict[task] = freq_dict.get(task, 0) + 1
        for task, freq in freq_dict.items():
            heapq.heappush(heap, [-freq, tasks])

        res = []
        queue, time = [], 0
        while heap or queue:
            if queue and time >= queue[0][0]:
                _, freq, task = queue.pop(0)
                heapq.heappush(heap, [freq, task])
            elif heap:
                freq, task = heapq.heappop(heap)
                res.append(task)
                time += 1
                freq += 1
                if freq < 0:
                    queue.append([time+n, freq, task])
                # time += 1
            else:
                res.append(None)
                time += 1
            print(heap, queue, res)
        return len(res)