class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        return self.find_maximum_subarray(nums, 0, len(nums))[2]

    def find_max_crossing_subarray(self, a, low, mid, high):
        left_sum = float('-inf')
        sum = 0
        max_left = mid
        for i in range(mid, low-1, -1):
            sum = sum + a[i]
            if sum > left_sum:
                left_sum = sum
                max_left = i
        if left_sum == float('-inf'):
            left_sum = sum

        right_sum = float('-inf')
        sum = 0
        max_right = mid + 1
        for j in range(mid + 1, high):
            sum = sum + a[j]
            if sum > right_sum:
                right_sum = sum
                max_right = j

        if right_sum == float('-inf'):
            right_sum = sum

        return (max_left, max_right, left_sum + right_sum)

    def find_maximum_subarray(self, a, low, high):
        if high == 0 and low == 0:
            return (0,0,0)
        if high == low:
            return (low, high, a[low])
        else:
            mid = (low + high) // 2
            if mid == low:
                return (low, mid, a[low])

            (left_low, left_high, left_sum) = self.find_maximum_subarray(a, low, mid)
            (right_low, right_high, right_sum) = self.find_maximum_subarray(a, mid, high)
            (cross_low, cross_high, cross_sum) = self.find_max_crossing_subarray(a, low, mid, high)

            if left_sum >= right_sum and left_sum >= cross_sum:
                return (left_low, left_high, left_sum)
            elif right_sum >= left_sum and right_sum >= cross_sum:
                return (right_low, right_high, right_sum)
            else:
                return (cross_low, cross_high, cross_sum)

    def solution1(self, nums):
        n = len(nums)
        s = nums[0]
        max_sum = s
        for i in range(1, n):
            s = s + nums[i]
            if nums[i] > s:
                s = nums[i]
            if s > max_sum:
                max_sum = s
        return max_sum


s = Solution()
#print(s.solution1([-2,1,-3,4,-1,2,1,-5,4]))
#print(s.maxSubArray([13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]))
print(s.maxSubArray([]))