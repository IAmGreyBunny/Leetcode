# Last updated: 12/12/2025, 3:05:54 PM
1class Solution:
2    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
3        # Declaring output 
4        answers = [[],[]]
5
6        # Edge cases
7        if len(nums1)<1 and len(nums2)<1:
8            return answers
9        elif len(nums1)<1:
10            answers[1] = nums2
11            return answers
12        elif len(nums2)<1:
13            answers[0] = nums1
14            return answers
15
16        # Log N search
17        def binarySearch(sorted_list,val):
18            if len(sorted_list) < 1:
19                return -1
20
21            low = 0
22            high = len(sorted_list)-1
23            mid = (low + high)//2
24
25            while(low<=high):
26                if sorted_list[mid] == val:
27                    return mid
28                elif val > sorted_list[mid]:
29                    low = mid + 1
30                    mid = (low + high)//2
31                elif val < sorted_list[mid]:
32                    high = mid - 1
33                    mid = (low + high)//2
34
35            return -1
36            
37        # n log n sort
38        nums1 = set(nums1) # Remove duplicates
39        nums2 = set(nums2) # Remove duplicates
40        answers[0] = list(nums1)
41        list.sort(answers[0])
42
43        print(f"answers 0: {answers[0]}")
44        
45
46        # loop through nums2
47        for num in nums2:
48            found = binarySearch(answers[0],num)
49
50            # Exists in nums 1
51            if found != -1:
52                print(f"{answers[0][found]} Found")
53                answers[0].pop(found)
54            else:
55                answers[1].append(num)
56        
57        print("Result")
58        print(f"{answers[0]}")
59        print(f"{answers[1]}")
60        return answers
61
62        
63