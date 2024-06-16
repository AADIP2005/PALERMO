tem=float(input("ENTER THE TEMPERATURE:"))
ch=int(input("ENTER UR CHOICE:"))
result=0
print("1.celsius to farenhite 2.farehite to celsius")
if ch==2:
    result=(tem-32)*5/9
    print("farehhite to celsius:",result)
if ch==1:
    result=(tem*9/5)+32
    print("cesius to farehntie:",result)

'''
ENTER THE TEMPERATURE:45
ENTER UR CHOICE:1
1.celsius to farenhite 2.farehite to celsius
cesius to farehntie: 113.0
PS C:\Users\aditi pandit\Desktop\PALERMO> & C:/msys64/ucrt64/bin/python.exe "c:/Users/aditi pandit/Desktop/PALERMO/23.py"
ENTER THE TEMPERATURE:45
ENTER UR CHOICE:2
1.celsius to farenhite 2.farehite to celsius
farehhite to celsius: 7.222222222222222
'''
