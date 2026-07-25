'''
OPERAtors:
->operators are symbols keywords that are used to perform opearation
    between operands(varible/value) and gives result
classifies as follws-
1)arthmatic
2)assignment->its used to assign value to the varible
3)relational->it is used to compare the values and variable(==,!=,>,<,<=,>=)
4)logical->they are used for evaluating conditions or combining multiple conditions, return boolean values(and, or, not)
5)identity-> memory comparision(is, is not)
6)membership->it is used to check if an element is member of sequence or collection(in, not in)
7)bitwise->it is used to perform bitwise operation on binary digits of decimal number.
        *)bitwise AND (&)->compare 2-bits and return 1 if both bits are 1.
        *)bitwise OR (|)->it comapre 2 bits and return 1 if atleast one bit is 1.
        *)bitwise XOR (^)->it compare 2 bits and return 1 if both bits are different
        *)bitwise NOT (~)->it inverts the bits(1 becomes 0 and 0 becomes 1)
        *)bitwise leftshift (<<)->it shifts bits to left side based on the Number of Positions
        *)bitwise rightshift (>>)->it shifts bits ti right side based on the number of positions

'''
'''
#print(5+5,5-2,5*2,5/2,5//2,5%2,5**2)
a=9
a+=9
print(a)
a-=8
print(a)
a*=9
print(a)
a/=4
print(a)
a//=4
print(a)
a%=3
print(a)
a**=9
print(a)

print(3==4)
print(4!=5)
print(2<4)
print(3>9)
print(34<=344)
print(21>=999)
'''
'''
print(True and True)
print(False and True)
print(True or True)
print(False or True)
print(not True)
print(not False)
print('False' and 'True')
print(5 or 30)

#membership oprator
l=[10,20,30,45,63]
print(45 in l)
print(89 in l)
d={1:10,2:20,3:30,4:40}
print(10 in d)# mainly it only check with keys
print(4 in d)
print(30 in d.values())#to check for values use the .values() function
'''

#bitwise
print(12&5)
print(12|5)
print(12^5)
print(~12)
print(12<<5)
print(12>>2)
