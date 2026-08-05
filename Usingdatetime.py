from datetime import date
Year=int(input("The year you were born in is : "))
Month=int(input("The month you were born in is : "))
Day=int(input("The day you were born in is : "))
print("your age is :",date.today().year-Year,"years old and",date.today().month-Month,"months old and",date.today().day-Day,"days old .")
