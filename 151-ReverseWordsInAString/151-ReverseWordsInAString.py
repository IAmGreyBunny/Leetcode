# Last updated: 11/30/2025, 5:39:58 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        list_string = list(s)
        word_stack = []

        word = ""
        for char in list_string:
            if char.isalnum():
                word+=char
            else:
                if word != "":
                    word_stack.append(word)
                word = ""
            
        if word != "":
            word_stack.append(word)

        result = ""
        while len(word_stack):
            word = word_stack.pop()
            if result != "":
                result += " " 
            result += word
        return result