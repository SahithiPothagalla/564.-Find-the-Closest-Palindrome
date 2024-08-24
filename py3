class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def findPalinFromLeft(leftHalf:int, isEvenLen:bool):
            x=str(leftHalf)
            if isEvenLen:
                x=x+x[::-1]
                return int(x)
                    
            y=x[:len(x)-1]
            z=x+y[::-1]
            return int(z) 
        
        l=len(n)
        lst = [findPalinFromLeft( int(str(n)[:ceil(l/2)]) , l%2==0), 
               findPalinFromLeft( (int(str(n)[:ceil(l/2)])-1), l%2==0 ), 
               findPalinFromLeft( (int(str(n)[:ceil(l/2)])+1), l%2==0 ), 
               10**l+1, 
               10**(l-1)-1 ]

        ans=float('inf')
        diff=float('inf')

        for i in lst:
            curr=abs(int(n)-i)
            if curr<diff and curr!=0:
                diff=curr
                ans=i
            elif curr==diff and curr!=0:
                ans=min(ans,i)
        
        return str(ans)
