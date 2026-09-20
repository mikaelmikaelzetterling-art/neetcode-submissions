class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        test = set()

        for i in range(len(nums) - 2):
            n = i + 1
            m = 1

            while n < len(nums) - m:
                summa = nums[i] + nums[n] + nums[len(nums) - m]

                if summa == 0:
                    svar = (
                        nums[i],
                        nums[n],
                        nums[len(nums) - m]
                    )

                    test.add(svar)

                    n += 1
                    m += 1

                elif summa < 0:
                    n += 1

                elif summa > 0:
                    m += 1

        slutsvar = [list(x) for x in test]

        return slutsvar