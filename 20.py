lst=[]
n=int(input("enter number of elements"))
sum=0
for i in range(n):
    ele=int(input())
    lst.append(ele)
    print(lst)
for i in lst:
    sum=sum+i
    print(sum)

'''
PS C:\Users\aditi pandit\Desktop\PALERMO> & C:/msys64/ucrt64/bin/python.exe "c:/Users/aditi pandit/Desktop/PALERMO/20.py"
enter number of elements4
1
[1]
2
[1, 2]
3
[1, 2, 3]
4
[1, 2, 3, 4]
1
3
6
10
'''