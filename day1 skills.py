# def reversenum(num):
#     temp = num
#     rev= 0
#     while temp > 0:
#         remainder = temp % 10
#         rev = (rev * 10) + remainder
#         temp = temp // 10
#     if num == rev:
#         print('Palindrome')
#     else:
#         print("Not Palindrome")
#
# num=1221
# result=reversenum(num)

def strStr(haystack, needle):
    if not needle:
        return 0
    if needle in haystack:
        return haystack.index(needle)
    return -1

haystack = "sadbutsad"
needle = "sad"
result=strStr(haystack, needle)
print(result)
