# Last updated: 12/14/2025, 10:45:00 AM
1class RecentCounter:
2
3    def __init__(self):
4        self.recent_reqs = []
5        self.last_req_index = -1
6        
7    def ping(self, t: int) -> int:
8        self.recent_reqs.append(t)
9        recent_reqs=self.recent_reqs
10        
11        
12        for req_index in range(0,len(recent_reqs)):
13            if recent_reqs[req_index] >= t-3000:
14                self.last_req_index = req_index
15                break
16    
17        return len(recent_reqs)-self.last_req_index
18        
19
20
21# Your RecentCounter object will be instantiated and called as such:
22# obj = RecentCounter()
23# param_1 = obj.ping(t)