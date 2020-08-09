class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        res = []

        def gui(num):
            if num == 0:
                return
            res.insert(0, num % 10)
            num = num - num % 10
            if num > 0:
                num = num / 10
            gui(num)
        gui(x)
        i, j = 0, len(res) - 1
        while i < j:
            if res[i] != res[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    print(Solution().isPalindrome(10))
