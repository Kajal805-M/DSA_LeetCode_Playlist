class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        if "()" in s:
            return self.isValid(s.replace("()",""))
        if "{}" in s:
            return self.isValid(s.replace("{}",""))
        if "[]" in s:
            return self.isValid(s.replace("[]",""))
        return False
       