class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num in count:
            frequency = count[num]
            buckets[frequency].append(num)

        resultat = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                resultat.append(num)

                if len(resultat) == k:
                    return resultat