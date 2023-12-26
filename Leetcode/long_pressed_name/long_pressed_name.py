class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # Define two pointer one for name and the other for typed
        ni = 0
        ti = 0

        # Loop condition it has to be a while for two pointers
        while ni <= len(name) and ti < len(typed):
            # If the same char sum 1 for both pointers
            # Is important that the n pointer is always smaller than the length of the string name
            if ni < len(name) and typed[ti] == name[ni]:
                ti += 1
                ni += 1
            # If the chars are not equal but the one in typed is equal to the previous one in name
            # sum 1 to the typed pointer, check that n1 pointer is different that 0 for diferences in the first char
            elif typed[ti] == name[ni-1] and ni != 0:
                ti += 1
            else:
                return False
        
        return ni == len(name) and ti == len(typed)
