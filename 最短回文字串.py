'''
在字符串前面添加字符，使其变成回文子串，得到最短的回文字串
思路：
（1）当前字符根据前一字符形成回文子串的结果上进行推导，比如i-1处可以和以2，4，5为开始形成的子串为回文串，那么
比较当前子符是否与1，3，4处的字符相等，若相等则可以形成回文
（2）初始化dp数组的
'''


def shortestPalindrome(s):
    s = list(s)
    size = len(s)
    if len(s) == 1:
        return s
    elif len(s) == 2:
        s.insert(0, s[-1])
    else:
        for i in range(1, s):

            huiwen()


if __name__ == '__main__':
    s = 'cdbbba'
    shortestPalindrome(s)
