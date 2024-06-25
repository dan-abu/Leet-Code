# Question can be found using this link: https://leetcode.com/problems/longest-common-prefix/description/
# Solution below

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
            commonPrefs = []
            strOne = strs[0]
            limit = len(min(strs, key=len))

            if len(strs) == 1:
                return strs[0]
            elif strOne == "":
                return strOne
            elif limit == 0:
                return "".join(commonPrefs)
            else:
                for i in range(limit):
                    for string in strs:
                        if strOne[i] == string[i]:
                            continue
                        else:
                            return "".join(commonPrefs)
                    commonPrefs.append(strOne[i])
                    continue
                return "".join(commonPrefs)