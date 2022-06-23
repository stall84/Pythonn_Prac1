class Solution:
    def isPalindrome(self, x: int) -> bool:
        # base conditions
        strinified = str(x)
        listified = list(strinified)
        print('listitified: ', listified)
        first = listified[0]
        last = listified[-1]
        if first == last:
            self.isPalindrome(listified)

        return False


flerp = Solution()

flerp.isPalindrome(3030)
