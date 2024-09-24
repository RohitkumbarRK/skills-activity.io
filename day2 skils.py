def hyphenssort(s):
    alpha=s.replace('_','')
    hyphen=s.count('_')
    return '_'*hyphen+alpha

result=hyphenssort("hello_hi_sir")
print(result)

# N-base notation
n=int(input())
num=int(input())
reminder=[]
q=num//n
reminder.append(num%n)
while q!=0:
    reminder.append(q%n)
    q=q//n
reminder=reminder[::-1]
equi=''
for i in reminder:
    if i>9:
        a=i-9
        a=64+a
        equi+=chr(a)
    else:
        equi+=str(i)
print(equi)
print(reminder)

 # password
 def password(pw):
     while True:
         if len(pw)<8:
             return 0
         elif pw[0].isdigit():
             return 0
         elif pw.isupper():
             return 1
         elif "/" in pw or " " in pw:
             return 0
         elif "@" in pw or "#" in pw or "$" in pw:
             return 1

# difference of sum

n=int(input())
m=int(input())
num1=[]
num2=[]
for i in range(1,m+1):
    if i%n==0:
        num1.append(i)
    else:
        num2.append(i)
res1=sum(num1)
res2=sum(num2)
res=abs(res1-res2)
print(res)

# largest and smallest element segrigated eventually in the even and odd and the sorted and adding the second largest and snallest number
def largestsmallnum(arr):
    arr_sorted=sorted(arr)
    print(arr_sorted)
    even=arr_sorted[::2]
    odd=arr_sorted[1::2]
    even.sort(reverse=True)
    odd.sort()
    return (even[2]+odd[2])
arr=[3,2,1,7,5,4,8,6,9,13]
result=largestsmallnum(arr)
print(result)

# smallest pair
def smllestpair(arr,sum):
    arr.sort()
    if len(arr)<2:
        return -1
    if arr[0]+arr[1]<=sum:
        return arr[0]*arr[1]
    else:
        return 0
arr=[4,1,6,7,8]
sum=3
result=smllestpair(arr,sum)
print(result)

# absolute count
def absolute(arr, num, diff):
    count=0
    for i in range(len(arr)):
        if abs(arr[i]-num)<=diff:
            count+=1
    if count==0:
        return -1
    else:
        return count

arr=[12,3,14,56,77,13]
result=absolute(arr, 13, 2 )
print(result)

# valid parentheses
def isValid(s):
    dict1 = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for i in s:
        if i in dict1:
            stack.append(dict1[i])
        else:
            if not stack or stack[-1] != i:
                return False
            stack.pop()
    if len(stack) == 0:
        return False
    else:
        return True


isValid("()")












