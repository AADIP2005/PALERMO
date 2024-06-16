def factorial(n):
    if (n==1 or n==0):
        return 1
    else:
        a=n*factorial(n-1)
        return a
    
num=int(input("enter the number:"))
print("factorial of",num,"is",factorial(num))

'''
PS C:\Users\aditi pandit\Desktop\PALERMO> & C:/msys64/ucrt64/bin/python.exe "c:/Users/aditi pandit/Desktop/PALERMO/3.py"
enter the number:3
factorial of 3 is 6
'''