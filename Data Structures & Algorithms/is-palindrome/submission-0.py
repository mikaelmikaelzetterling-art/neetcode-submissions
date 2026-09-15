class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
            ]


        s = s.lower()
        new_s = ''
        modifierad_s = ''  

        for i in range(len(s) - 1, -1, -1):
            if s[i] in letters:
                new_s += s[i]
        
        for i in range(0,len(s), 1 ):
            if s[i] in letters:
                modifierad_s += s[i]


        if modifierad_s == new_s:
            return True
        else:
            return False
        