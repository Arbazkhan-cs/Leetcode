class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        st = sorted(strs)

        first_st = st[0]
        last_st = st[-1]

        for i in range(min(len(first_st), len(last_st))):
            if first_st[i] != last_st[i]:
                return first_st[:i]
        return first_st