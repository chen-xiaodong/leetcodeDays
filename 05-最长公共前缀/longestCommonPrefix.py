class Solution:
    def longestCommonPrefix(self, strs: List[str]):
        if not strs: return ""
        length_list = []
        res = ''
        for str in strs:
            length = len(str)
            length_list.append(length)
        flag = length_list.index(min(length_list))
        result = strs[flag]
        strs.remove(result)
        for i, each_char in enumerate(result):
            for str2 in strs:
                if str2[i] != each_char:
                    return res
            res = res + each_char
        return res
