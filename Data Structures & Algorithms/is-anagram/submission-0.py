class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary1 = {}
        dictionary2 = {}
        for i in s:
            if i in dictionary1:
                dictionary1[i] += 1
            else:
                dictionary1[i] = 1
        
    

        for i in t:
            if i in dictionary2:
                dictionary2[i] += 1
            else:
                dictionary2[i] = 1
        
        return dictionary1 == dictionary2