class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = 0
        m = 1

        while n < len(numbers) - m:
            summa = numbers[n] + numbers[len(numbers) - m]

            if summa < target:
                n += 1

            elif summa > target:
                m += 1

            else:
                return [n + 1, len(numbers) - m + 1]