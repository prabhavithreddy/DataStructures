class Solution:
    """
    @param s: a string
    @param t: a string
    @return: the minimum substring of S
    """


    def min_window(self, s: str, t: str) -> str:
        # Write your code here
        if len(t) == 0 or len(s) == 0 or len(t) > len(s):
            return "unable to match"

        indexes = []

        first_char = t[0]
        shortest = s

        for i in range(len(s)):
            if s[i] == first_char:
                indexes.append(i)

        if len(indexes) == 0:
            return "unable to match"
        indexes.append(len(s))
        shortest_index = indexes[0]



        for i in range(len(indexes) - 1):
            lower = indexes[i]
            upper = indexes[i + 1]
            incr = lower
            current = 0
            while incr < upper:
                if s[incr] == t[current]:
                    current += 1
                if current == len(t):
                    substr = s[lower:incr + 1]
                    if len(substr) == len(shortest) and lower > shortest_index:
                        shortest = substr
                    elif len(substr) < len(shortest):
                        shortest = substr
                    shortest_index = lower
                    break
                incr += 1

        return shortest

    def min_window1(self, s: str, t: str) -> str:
        # Write your code here
        if len(t) == 0 or len(s) == 0 or len(t) > len(s):
            return "unable to match"

        indexes = []

        first_char = t[0]
        shortest = s

        if t[0] not in s:
            return "unable to match"

        n = len(s)
        shortest_index = 0
        i = 0
        current = 0
        prev_index = 0
        while i < n:
            if s[i] != t[current]:
                i+=1
            else:
                if current == 0:
                    prev_index = i
                current += 1
                if current == len(t):
                    substr = s[prev_index:i+1]
                    if len(substr) == len(shortest) and prev_index > shortest_index:
                        shortest = substr
                    elif len(substr) < len(shortest):
                        shortest = substr
                    shortest_index = prev_index
                    current = 0
                i+=1
        return shortest

    def min_window2(self, s: str, t: str) -> str:
        # Write your code here
        if len(t) == 0 or len(s) == 0 or len(t) > len(s):
            return "unable to match"

        indexes = []

        first_char = t[0]
        shortest = s
        exists = False
        n = len(s)
        for i in range(len(s)):
            if s[i] == first_char:
                indexes.append(i)

        if len(indexes) == 0:
            return "unable to match"

        for i in range(len(indexes)):
            lower = indexes[i]
            incr = lower
            current = 0
            substr = ""
            while incr < n:
                if s[incr] == t[current]:
                    current += 1
                if current == len(t):
                    exists = True
                    substr = s[lower:incr + 1]
                    if len(substr) < len(shortest):
                        shortest = substr
                    break
                incr += 1
        if not exists:
            return "unable to match"
        return shortest


s = Solution()

print(s.min_window2("abcdebdde", 'bdx'))