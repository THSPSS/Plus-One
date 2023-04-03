class Solution:
    def defangIPaddr(self, address: str) -> str:
        # first solution
        # using replace "." to "[.]"

        # The replace() method replaces a specified phrase with another specified phrase.
        # return address.replace(".","[.]")
        # put () and memory reduced from 13.8 to 13.6
        return (address.replace(".", "[.]"))