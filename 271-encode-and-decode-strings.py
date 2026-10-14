#logic: do number of chars+delimiter+string, and just check that
#make strings of the length of the ints before the delimiter
#time complexity of encode (O(N))
#time complexity of decode (O(N))
#space complexity of both is O(N) as well

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res = res+str(len(i))+"#"+i
        return res

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        output=[]
        ptr1 = 0
        ptr2 = 1
        while ptr1 < len(s):
            while ptr2 < len(s) and s[ptr2] != "#":
                ptr2+=1
            ct=int(s[ptr1:ptr2])
            out=s[ptr2+1:ptr2+ct+1]
            output.append(out)
            ptr1=ptr2+ct+1
            ptr2=ptr1+1
        return output