class Solution:
    def isPalindrome(self, s: str) -> bool:
        #logic for doing it simply by just using str[::-1]
        # ns = ""
        # for c in s:
        #     if c.isalnum():
        #         ns+=c.lower()
        
        # return ns==ns[::-1]
        
        #logic is making our own isalnum() function using ord
        #time complexity is O(N) because we just iterate through half the string
        #auxiliary space complexity is O(1) because we dont build another string
        l=0
        r=len(s)-1
        while l<r:
            if not self.alnum(s[r]):
                r-=1
            elif not self.alnum(s[l]):
                l+=1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                else:
                    l+=1
                    r-=1
        return True

    def alnum(self, c):
        if (ord('A') <= ord(c) <= ord('Z') or
        ord('a') <= ord(c) <= ord('z') or
        ord('0') <= ord(c) <= ord('9')):
            return True
        else: return False
