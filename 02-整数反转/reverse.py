class Solution:
    def reverse(self, x: int):
        if -10 < x < 10:
            return x
        else:
            str_x = str(x)
            if str_x[0] != '-':
                result = str_x[::-1]
                x = int(result)
            else:
                result = str_x[-1:0:-1]
                x = int(result)
                x = -x
            return x if -2147483648 < x < 2147483647 else 0
