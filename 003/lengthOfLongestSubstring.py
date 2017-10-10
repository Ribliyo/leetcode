import random
import string

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        m = 0
        dict = {}
        for idx, c in enumerate(s):
            if c in dict:
                start = max(start, dict[c] + 1)
            dict[c] = idx
            dist = idx - start + 1
            m = max(dist, m)
        return m

    def stupid(self, s):
        m = 0
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        for i in range(len(s)):
            words = set(s[i])
            for j in range(i + 1, len(s)):
                if s[j] in words:
                    m = max(m, j - i)                    
                    break
                else:
                    words.add(s[j])
                    m = max(m, j - i + 1)
        return m

if __name__ == '__main__':
    s = Solution()
    for i in range(1000):
        N = random.randrange(1, 10)
        str = ''.join(random.choice(string.ascii_lowercase) for _ in range(N))
        n1 = s.lengthOfLongestSubstring(str)
        n2 = s.stupid(str)
        if n1 != n2:
            print(str, n1, n2, n1 == n2)


