'''
Print() :
->it is the predefined function in pytohn which is used to display the output on the console(screen)
->it is possible to display multiple values using single print fucntion

2-default arguments of print fucntion:
    1)sep->whenever multiple values seperated by comma are printed, the value of
        sep will be printed after each value
        print(v1,v2,v3,v4,sep=" ")
    2)end->once the all values are displayed, value of end will be printed at the last only once
        -default value of end is \n, end="\n"

'''

print(10,20,30)
print(10)
print(20)
print(30)
print(10,20,203,493,2423,23445,43,sep=" ")
print(10,20,203,493,2423,23445,43,sep="###3")

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(10,20,203,493,2423,23445,43,end="\n")

print(13,14,15,16,sep="\n",end="@")
print(20,end="\n")
print(30,40,sep="\n",end="")
print(70)
