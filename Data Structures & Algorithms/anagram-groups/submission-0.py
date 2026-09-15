class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grupper = {}

        for word in strs:
            counts = {}

            for bokstav in word:
                if bokstav in counts:
                    counts[bokstav] += 1
                else:
                    counts[bokstav] = 1

            key = []

            for i in range(26):
                bokstav = chr(ord("a") + i)

                if bokstav in counts:
                    key.append(counts[bokstav])
                else:
                    key.append(0)

            key = tuple(key)
            if key not in grupper:
                grupper[key] = []

            grupper[key].append(word)

        return list(grupper.values())