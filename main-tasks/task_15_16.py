# Get the user's input
basic_salary = float(input("Enter your basic salary: "))
benefits = float(input("Enter your benefits: "))

# Calculate the gross salary
gross_salary = basic_salary + benefits

# Calculate NHIF contribution
if gross_salary <= 5999:
    NHIF_contribution = 150
elif 6000 <= gross_salary <= 7999:
    NHIF_contribution = 300
elif 8000 <= gross_salary <= 11999:
    NHIF_contribution = 400
elif 12000 <= gross_salary <= 14999:
    NHIF_contribution = 500
elif 15000 <= gross_salary <= 19999:
    NHIF_contribution = 600
elif 20000 <= gross_salary <= 24999:
    NHIF_contribution = 750
elif 25000 <= gross_salary <= 29999:
    NHIF_contribution = 850
elif 30000 <= gross_salary <= 34999:
    NHIF_contribution = 900
elif 35000 <= gross_salary <= 39999:
    NHIF_contribution = 950
elif 40000 <= gross_salary <= 44999:
    NHIF_contribution = 1000
elif 45000 <= gross_salary <= 49999:
    NHIF_contribution = 1100
elif 50000 <= gross_salary <= 59999:
    NHIF_contribution = 1200
elif 60000 <= gross_salary <= 69999:
    NHIF_contribution = 1300
elif 70000 <= gross_salary <= 79999:
    NHIF_contribution = 1400
elif 80000 <= gross_salary <= 89999:
    NHIF_contribution = 1500
elif 90000 <= gross_salary <= 99999:
    NHIF_contribution = 1600
else:
    NHIF_contribution = 1700

# Calculate NHDF contribution
NHDF_rate = 0.015
NHDF_contribution = gross_salary * NHDF_rate

print("Your gross salary is:", gross_salary)
print("Your NHIF contribution is:", NHIF_contribution)
print("Your NHDF contribution is:", NHDF_contribution)
