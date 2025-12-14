# Last updated: 12/14/2025, 10:41:49 AM
1class RecentCounter:
2
3    def __init__(self):
4        self.recent_reqs = []
5        
6    def ping(self, t: int) -> int:
7        self.recent_reqs.append(t)
8        recent_reqs=self.recent_reqs
9        last_req_index = -1
10        
11        for req_index in range(0,len(recent_reqs)):
12            if recent_reqs[req_index] >= t-3000:
13                last_req_index = req_index
14                break
15    
16        return len(recent_reqs)-last_req_index
17        
18
19
20# Your RecentCounter object will be instantiated and called as such:
21# obj = RecentCounter()
22# param_1 = obj.ping(t)