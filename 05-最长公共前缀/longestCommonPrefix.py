class Solution:
    def longestCommonPrefix(self, strs: List[str]):
        """
        整体解决方案：通过取出字符串列表中最短字符串，然后拆解该字符串去其他字符串中进行比对
        一旦不在其他字符串中，立刻返回空值

        :param strs:
        :return:

        """
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
