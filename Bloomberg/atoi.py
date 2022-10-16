class Solution:
    def myAtoi(self, s: str) -> int:
        sign_characters = ['+', '-']
        valid_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        int_max = 2147483648
        sign = False
        result = 0
        i = 0
        n = len(s)

        if n == 0:
            return 0

        while i < n and s[i] == " ":
            i += 1

        if i < n:
            sign = s[i]
            if sign in sign_characters:
                if sign == "-":
                    sign = True
                i += 1

        while i < n and s[i] in valid_characters:
            result = 10 * result + (ord(s[i]) - ord('0'))
            i += 1

        if sign == True:
            return max(-1 * int_max, -1 * result)
        else:
            return min(int_max - 1, result)
