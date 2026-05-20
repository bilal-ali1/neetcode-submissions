class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [n1*n2*n3, n0*n2*n3, n0*n1*n3, n0*n1*n2]

        # [1         n0        n0*n1     n0*n1*n2]
        # [n1*n2*n3  n2*n3      n3           1]

        # first loop:
        arr1 = [1 for num in nums]
        print(arr1)
        for i in range(1 ,len(nums)):
            arr1[i] = (arr1[i - 1] * nums[i - 1])
        
        arr2 = [1 for num in nums] # [1, 1, 1, 1]
        print(arr2)
        for i in range(len(nums) - 2, -1, -1):
            arr2[i] = nums[i + 1] * arr2[i + 1]


        print(arr1)
        print(arr2)
        final_arr = []
        for i in range(len(nums)):
            final_arr.append(arr1[i] * arr2[i])

        return final_arr

        