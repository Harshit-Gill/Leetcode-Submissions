class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        temp = []
        n = len(nums)
        k %= n
        
        for i in range(n-k,n):
            temp.append(nums[i])
       

        #shifting
        for i in range(n-1,k-1,-1):
            nums[i] = nums[i-k]
            
        
        #put back temp

        for i in range(0,k):
            nums[i] = temp[i]
            