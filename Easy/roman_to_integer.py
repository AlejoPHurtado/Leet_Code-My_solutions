class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        x = len(s)
        n = 0
        for i in range(x):
            if i < x - 1 and m[s[i]] < m[s[i+1]]:
                n -= m[s[i]]
            else:
                n += m[s[i]]
        return n
