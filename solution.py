class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split_str = s.split()
        return len(split_str[-1])
        
