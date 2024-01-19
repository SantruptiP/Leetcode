class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res1 = ''.join(sorted(s))
        res2 = ''.join(sorted(t))
        if res1==res2:
            return True
        else:
            return False