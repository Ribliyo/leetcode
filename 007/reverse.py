class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        magic = ((1 << 31) - 1) / 10
        print magic
        r = 0
        sign = x > 0
        x = abs(x)
        while x > 0:
            digit = x % 10
            x = x / 10
            if r > magic:
                return 0
            r = r * 10
            r += digit
        return r if sign else -r

if __name__ == "__main__":
    import random
    import string
    s = Solution()
    for i in range(100):
        N = random.randrange(1, 10)
        randomN = ''.join(random.choice(string.digits) for _ in range(N))
        neg = random.randrange(1, 10)
        num = int(randomN) if neg >= 3 else -int(randomN)
        print(num, s.reverse(num), randomN[::-1])
    max_num = ((1 << 31) - 1)
    max_num_str = str(max_num/10) + "9"
    max_num_str = max_num_str[::-1]
    print(s.reverse(int(max_num_str)))
    print(s.reverse(1534236469))
