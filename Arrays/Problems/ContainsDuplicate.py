from joblib import Parallel, delayed

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        threads = 4
        results = Parallel(n_jobs=threads)(delayed(self.hasDuplicate)
                                           (nums[i * threads: (i + 1) * threads]) for i in
                                           range(len(nums) // threads + 1))
        result = False
        for r in results:
            result = result or r

        return result

    def hasDuplicate(self, numbers):
        if len(numbers) > 0:
            frequency = {}
            for num in numbers:
                if num is None:
                    continue
                if num not in frequency:
                    frequency[num] = 0
                frequency[num] += 1
                if frequency[num] >= 2:
                    return True

            return False
        else:
            return False