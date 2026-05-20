class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = {}
        for i in range(len(nums)):
            if nums[i] in frequency_dict:
                frequency_dict[nums[i]] += 1
            else:
                frequency_dict[nums[i]] = 1
        return_list = []
        sorted_frequencies = sorted(frequency_dict.items(), key=lambda x:x[1], reverse=True)
        return [x[0] for x in sorted_frequencies][:k]

        

            