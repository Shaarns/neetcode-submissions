class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #[], time=9,n=3 [[, if 0 dont push]

        tasks_count = {}
        for task in tasks:
            tasks_count[task] = tasks_count.get(task, 0) + 1

        max_heap = [-1*val for val in tasks_count.values()]
        heapq.heapify(max_heap)
        print(max_heap)

        q = collections.deque()
        time = 0

        while max_heap or q:
            time += 1
            if max_heap:
                task = heapq.heappop(max_heap)
                task += 1

                if task != 0:
                    q.append([task, time+n])

            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

        return time
