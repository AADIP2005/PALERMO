import datetime
current_year=datetime.datetime.now().year
birth_year=input("ENTER YOUR BIRTH YEAR:")
birth_year=int(birth_year)
age=current_year-birth_year
print("you are",age,"years old.")