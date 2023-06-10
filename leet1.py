class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        x=[]
        for i in range(len(nums)):
            if nums[i]==target:
                x.append(i)
        if len(x)==0:
            return [-1,-1]
        elif len(x)==1:
            x.append(x[0])
            return x
        else:
            for i in range(len(x)):
                if len(x)>2:
                    x.pop(1)
            return x