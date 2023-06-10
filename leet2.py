class Solution:
    def reverse(self, x: int) -> int:
        m=x
        if x>0:
            z=0
            while x>0:
                y=x%10
                z=(z*10)+y
                x=x//10
        else:
            x=-x
            z=0
            while x>0:
                y=x%10
                z=(z*10)+y
                x=x//10
        if z>(2**31)-1 or z<-2**31:
            return 0
        else:
            if m>0:
                return z
            else:
                return -z