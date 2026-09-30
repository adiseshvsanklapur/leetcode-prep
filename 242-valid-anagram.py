class Solution:
    
    #hash map logic
    #store letters and counts as keys and values in hashmap
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {},{}
        
        for i in range(len(s)):
            countS[s[i]] = 1+countS.get(s[i], 0)
            countT[t[i]] = 1+countT.get(t[i], 0)

        for i in range(len(s)):
            if countS.get(s[i]) != countT.get(s[i]):
                return False

        return True

    #O(T)+O(S) where T is the length of string t
    #and S is the length of string s
    #space complexity: O(S)+O(T)

    # if asked to do a solution with O(1) memory
    # use sorting of the string to make sure its the same
    # but time complexity goes down

    # class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if sorted(s) == sorted(t):
    #         return True
    #     else:
    #         return False

    #time complexity: O(S log S) + O(T log T)
    #space complexity: O(1) if we don't consider
    #the space used by the sorting algorithm