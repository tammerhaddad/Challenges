class mySolution(object):
    def isAnagram(self, s, t):
        # just sorts and checks if equal
        return sorted(s) == sorted(t)
    
# Answer
class Solution(object):
    # uses a cool hashtable with letter frequencies
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        freq = [0] * 26
        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1
        
        for i in range(len(freq)):
            if freq[i] != 0:
# same as the last one, it just saves time by cutting the program if found false
                return False
        
        return True