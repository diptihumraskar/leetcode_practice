class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        next_greater = {}
        for num in nums2:

            while stack and num > stack[-1]:

                smaller = stack.pop()

                next_greater[smaller] = num

            stack.append(num)

    # Remaining elements have no next greater element

        while stack:

            next_greater[stack.pop()] = -1

        return [next_greater[num] for num in nums1]
        