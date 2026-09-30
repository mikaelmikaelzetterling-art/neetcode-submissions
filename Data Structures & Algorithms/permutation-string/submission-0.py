class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target = {}

        for i in s1:
            target[i] = target.get(i, 0) + 1

        window_dict = {}

        for i in s2[:len(s1)]:
            window_dict[i] = window_dict.get(i, 0) + 1

        for left in range(len(s2) - len(s1) + 1):

            if window_dict == target:
                return True

            if left + len(s1) < len(s2):

                old_char = s2[left]
                window_dict[old_char] -= 1

                if window_dict[old_char] == 0:
                    del window_dict[old_char]

                new_char = s2[left + len(s1)]
                window_dict[new_char] = window_dict.get(new_char, 0) + 1

        return False