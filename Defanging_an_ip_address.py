class Solution:
    def defangIPaddr(self, address: str) -> str:
        # first solution
        # using replace "." to "[.]"
        # return address.replace(".","[.]")
        # put () and memory reduced from 13.8 to 13.6
        return (address.replace(".", "[.]"))