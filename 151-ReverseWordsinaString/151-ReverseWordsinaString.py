# Last updated: 12/4/2025, 2:06:08 PM
1class Solution:
2    def reverseWords(self, s: str) -> str:
3        list_string = list(s)
4        word_stack = []
5
6        word = ""
7        for char in list_string:
8            if char.isalnum():
9                word+=char
10            else:
11                if word != "":
12                    word_stack.append(word)
13                word = ""
14            
15        if word != "":
16            word_stack.append(word)
17
18        result = ""
19        while len(word_stack):
20            word = word_stack.pop()
21            if result != "":
22                result += " " 
23            result += word
24        return result