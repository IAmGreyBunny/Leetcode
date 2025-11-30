# Last updated: 11/30/2025, 5:39:50 PM
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        result = []
        cur_char = chars[0]
        count = 0 

        for char in chars:
            if char == cur_char:
                count+=1
            else:
                result.append(str(cur_char))
                if count>1:
                    count = str(count)
                    for digit in count:
                        result.append(digit)
                print("char: " + char +" ,count: " + str(count))
                print(result)
                cur_char = char
                count = 1
            

        result.append(str(cur_char))
        if count>1:
            count = str(count)
            for digit in count:
                result.append(digit)
        print("char: " + str(cur_char) +" ,count: " + str(count))
        print(result)
        
        chars[:] = result
        return len(chars)

        