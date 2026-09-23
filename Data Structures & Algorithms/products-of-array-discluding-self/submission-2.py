class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = []
        prefix_prod_inv = []
        prod = 1
        for val in nums : 
            prod *= val 
            prefix_prod.append(prod)
        prod = 1
        for val in nums[::-1]:
            prod *= val
            prefix_prod_inv.append(prod)
        prefix_prod_inv.reverse()

        exclusive_product = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            left_element = prefix_prod[i-1] if i-1 >= 0 else 1
            right_element = prefix_prod_inv[i+1] if i+1 < len(nums)  else 1
            exclusive_product[i] = int(left_element*right_element)
        return exclusive_product