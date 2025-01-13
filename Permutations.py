class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 0:
            return [[]]

        permutations_without_first_element = self.permute(nums[1:])

        res = []

        for permutation in permutations_without_first_element:
            for i in range(len(permutation) + 1):
                temporal_perm = permutation.copy()
                temporal_perm.insert(i, nums[0])
                res.append(temporal_perm)

        return res
