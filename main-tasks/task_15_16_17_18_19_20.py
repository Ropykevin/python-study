def calculate_gross(basic_salary=0, benefits=0):
    gross = basic_salary + benefits
    return gross

def calculate_nhif(gross_salary=0):
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
    return NHIF_contribution

def calculate_nhdf(gross_salary=0, nhdf_rate=0.015):
    NHDF_contribution = gross_salary * nhdf_rate
    return NHDF_contribution

def calculate_nssf(gross_salary=0, nssf_rate=0.06):
    gross_limit = 18000
    if gross_salary < 18000:
        nssf_contribution = gross_salary * nssf_rate
    else:
        nssf_contribution = gross_limit * nssf_rate
    return nssf_contribution

def calculate_total_nhdf_nssf(nssf,nhdf):
    total=nssf+nhdf
    return total

def calculate_taxable_income(gross_salary,nssf_nhdf_total):
    t_income=gross_salary-nssf_nhdf_total
    return t_income

def calculate_payee(taxable_income, personal_relief=2400):
    if taxable_income <= 24000:
        max_tax=24000
        payee_rate = 0.1
        gross_payee =  max_tax* payee_rate
    elif taxable_income <= 32333:
        payee_rate = 0.25
        gross_payee = (taxable_income - 24000) * payee_rate + 2400
    elif taxable_income <= 500000:
        payee_rate = 0.3
        gross_payee = (taxable_income - 32333) * payee_rate + 4483.25
    else:
        payee_rate = 0.35
        gross_payee = (taxable_income - 500000) * payee_rate + 19458.25

    net_payee = gross_payee - personal_relief
    return net_payee

def calculate_net_pay(gross_salary, nssf_nhdf_total, payee, nhif):
    net_salary = gross_salary - (nssf_nhdf_total + payee + nhif)
    return net_salary


# Getting user input for basic salary and benefits
basic_salary = float(input("Enter your basic salary: "))
benefits = float(input("Enter your benefits: "))

# Calculating contributions and deductions
gross_salary = calculate_gross(basic_salary, benefits)
nhif = calculate_nhif(gross_salary)
nhdf = calculate_nhdf(gross_salary)
nssf = calculate_nssf(gross_salary)
nssf_nhdf_total=calculate_total_nhdf_nssf(nssf,nhdf)
taxable_income=calculate_taxable_income(gross_salary,nssf_nhdf_total)
payee=calculate_payee(taxable_income)
net_pay=calculate_net_pay(gross_salary, nssf_nhdf_total, payee, nhif)

print("Your gross salary is:", gross_salary)
print("Your NHIF contribution is:", nhif)
print("Your NHDF contribution is:", nhdf)
print("Your NSSF contribution is:", nssf)
print("Your sum NSSF and NHDF contribution is:", nssf_nhdf_total)
print("Your Taxable income contribution is:", taxable_income)
print("Your PAYEE contribution is:", payee)
print("Your Net salary contribution is:", net_pay)
