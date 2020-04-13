'''
用动态规划实现最长回文字串是
如果只有一个字母肯定是回文字串
状态转移：大于2的回文字串，头尾各减去1还是回文字串

因此，如果一个字符串的头尾两个字符相等，才有必要继续判断下去
（1）如果里面的字串是回文，整体就是回文
（2）如果里面的子串不是回文，整体就不是回文串
定义状态：dp[i][j]表示字串s[i,j]是回文字串
状态转移方程：dp[i][j]=s[i+1,j-1]+s[i]==s[j]
分析这个状态转移方程：
（1）动态规划事实上是在填一张二维表格，i和j的关系是i<=j,因此只需要填表的上半部分就可以
（2）边界条件：[i+1,j-1]不构成区间，即严格小于2，j-i<3.当子串s[i,j]的长度等于2或者等于3时，只需要判断s[i]
是否和s[j]相等
'''


def longestPalindrome(s):
    # 初始化
    size = len(s)
    if size < 2:
        return s
    # 二维矩阵初始化 全初始化为False
    dp = [[False for _ in range(size)] for _ in range(size)]
    max_len = 1  # 记最大len
    start = 0  # 记start
    # 对角线肯定是回文字串
    for i in range(size):
        dp[i][i] = True
    # 遍历上半部分的子串
    for j in range(1, size):
        for i in range(0, j):
            if s[i] == s[j]:
                if j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = False
            if dp[i][j]:
                cur_len = j - i + 1
                if cur_len > max_len:
                    max_len = cur_len
                    start = i
    return s[start:start + max_len]
