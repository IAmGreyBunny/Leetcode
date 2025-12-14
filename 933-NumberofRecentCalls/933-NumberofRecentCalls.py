# Last updated: 12/14/2025, 11:29:28 AM
1class RecentCounter:
2
3    def __init__(self):
4        self.queue = deque()
5        
6    def ping(self, t: int) -> int:
7        self.queue.append(t)
8
9        # Remove outdated
10        while self.queue and self.queue[0] < t-3000:
11            self.queue.popleft()
12
13        return len(self.queue)
14
15# Your RecentCounter object will be instantiated and called as such:
16# obj = RecentCounter()
17# param_1 = obj.ping(t)