def romanToInt(s):
    count = 0
    dicts = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5,
             'IV': 4, 'I': 1}
    i = len(s)
    while i > 0:
        print(i)
        if s[i - 2:i] in dicts and i >= 2:
            count += dicts[s[i - 2:i]]
            i -= 2
        else:
            count += dicts[s[i - 1:i]]
            i -= 1
    return count


if __name__ == '__main__':
    print(romanToInt('III'))
