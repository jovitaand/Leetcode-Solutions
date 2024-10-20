class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".","[.]")
    #string.replace(old, new, count)//syntax