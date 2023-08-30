# write a program to check weather a number is divisible by 7
number=int(input("enter number:" ))
if number%7==0:
    print(f"{number }divisible by 7")
else:
    print(f"{number }not divisible by 7")
# write a program to calculate the electricity bill based on the following criteria
# unit 
# first 50 units ksh.20
# next 50 units  ksh.40
# after 100 units kshs.100
# unit=int(input("enter units:" ))
# if unit<=50:
#     electricity_bill=20
# elif unit>50 and unit<=100:
#     electricity_bill= 20+40
# else:
#     electricity_bill= 20+40+100
# print(electricity_bill)

unit=int(input("enter units:" ))
if unit<=50 and unit>0:
    electricity_bill=20*unit
elif unit>50 and unit<=100:
    electricity_bill= (unit-50)*40+1000
elif unit>100:
    electricity_bill= (unit-100)*100 + 2000+1000
else:
    electricity_bill= 0
print(f"{electricity_bill } ksh")