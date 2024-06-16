num1=int(input("ENTER NUM1:"))
num2=int(input("ENTER NUM2:"))
result=0
print("1.addition 2.subtraction 3.division 4.multipliaction")
choice=int(input("ENTER YOUR CHOICE:"))
if choice==1:
    result=num1+num2
    print("the sum of two numbers:",result)
if choice==2:
    result=num1-num2
    print("the subtration of two numbers:",result)
if choice==3:
    result=num1*num2
    print("the multiplication:",result)
if choice==4:
    result=num1/num2
    print("the division of two numbers:",result)

'''
PS C:\Users\aditi pandit\Desktop\PALERMO> & C:/msys64/ucrt64/bin/python.exe "c:/Users/aditi pandit/Desktop/PALERMO/24.py"
ENTER NUM1:10
ENTER NUM2:5
1.addition 2.subtraction 3.division 4.multipliaction
ENTER YOUR CHOICE:3
the multiplication: 50
PS C:\Users\aditi pandit\Desktop\PALERMO> & C:/msys64/ucrt64/bin/python.exe "c:/Users/aditi pandit/Desktop/PALERMO/24.py"
ENTER NUM1:10
ENTER NUM2:5
1.addition 2.subtraction 3.division 4.multipliaction  
ENTER YOUR CHOICE:4
the division of two numbers: 2.0
PS C:\Users\aditi pandit\Desktop\PALERMO> & C:/msys64/ucrt64/bin/python.exe "c:/Users/aditi pandit/Desktop/PALERMO/24.py"
ENTER NUM1:10
ENTER NUM2:5
1.addition 2.subtraction 3.division 4.multipliaction  
ENTER YOUR CHOICE:1
the sum of two numbers: 15
PS C:\Users\aditi pandit\Desktop\PALERMO>
PS C:\Users\aditi pandit\Desktop\PALERMO> & C:/msys64/ucrt64/bin/python.exe "c:/Users/aditi pandit/Desktop/PALERMO/24.py"
ENTER NUM1:10
ENTER NUM2:5
1.addition 2.subtraction 3.division 4.multipliaction  
ENTER YOUR CHOICE:2
the subtration of two numbers: 5

'''


    