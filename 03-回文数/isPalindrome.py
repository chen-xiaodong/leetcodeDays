class Solution:
    def isPalindrome(self, x: int):
        if x > 0:
            x_str = str(x)
            # 可以直接使用[：：-1]，进行字符串的反转
            x_list = list(x_str)
            if x_list[-1] == 0:
                '''
                这里处理最后一位可以有更好的办法
                x%10==0 取余判断最后一位
                
                '''

                return False
            x_list.reverse()
            str_a = "".join(x_list)
            if -2147483648 < int(str_a) < 2147483647:
                if str_a == x_str:
                    return True
            else:
                return False
        elif x==0:
            return True
        else:
            return False
