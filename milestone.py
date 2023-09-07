# # MILESTONE TASK Using Python or PHP or Java or Ruby or JavaScript
# # Create a class called Payroll whose major task is to calculate an individual’s Net Salary by getting the inputs basic salary and benefits.
# # Create 5 different class methods which will calculate the payee, nhif_deductions, nhdf_deductions, nssf_deductions, gross_salary and net_salary. 
# # NB: Use KRA, NHIF and NSSF values provided in the links above.
# #into a dictionary
class SalaryCalculator:
    details={}
    def __init__(self,basic_salary=0,benefit=0):
        self.basic_salary=int(basic_salary)
        self.benefits=int(benefit)
        self.calculate_gross()
        self.calculate_nhif()
        self.calculate_nssf()
        self.calculate_nhdf()
        self.total_nhdf_nssf()
        self.calculate_taxable_income()
        self.calculate_payee()
        self.calculate_net_pay()
        self.add()


    def calculate_gross(self):
        self.gross_salary=self.basic_salary+self.benefits


    def calculate_nhif(self):
        if self.gross_salary <= 5999:
            self.NHIF_contribution = 150
        elif 6000 <= self.gross_salary <= 7999:
            self.NHIF_contribution = 300
        elif 8000 <= self.gross_salary <= 11999:
            self.NHIF_contribution = 400
        elif 12000 <= self.gross_salary <= 14999:
            self.NHIF_contribution = 500
        elif 15000 <= self.gross_salary <= 19999:
            self.NHIF_contribution = 600
        elif 20000 <= self.gross_salary <= 24999:
            self.NHIF_contribution = 750
        elif 25000 <= self.gross_salary <= 29999:
            self.NHIF_contribution = 850
        elif 30000 <= self.gross_salary <= 34999:
            self.NHIF_contribution = 900
        elif 35000 <= self.gross_salary <= 39999:
            self.NHIF_contribution = 950
        elif 40000 <= self.gross_salary <= 44999:
            self.NHIF_contribution = 1000
        elif 45000 <= self.gross_salary <= 49999:
            self.NHIF_contribution = 1100
        elif 50000 <= self.gross_salary <= 59999:
            self.NHIF_contribution = 1200
        elif 60000 <= self.gross_salary <= 69999:
            self.NHIF_contribution = 1300
        elif 70000 <= self.gross_salary <= 79999:
            self.NHIF_contribution = 1400
        elif 80000 <= self.gross_salary <= 89999:
            self.NHIF_contribution = 1500
        elif 90000 <= self.gross_salary <= 99999:
            self.NHIF_contribution = 1600
        else:
            self.NHIF_contribution = 1700


    def calculate_nssf(self,nssf_rate=0.06):
        if self.gross_salary < 18000:
            self.nssf_contribution = self.gross_salary * nssf_rate
        else:
            self.nssf_contribution =18000*nssf_rate


    def calculate_nhdf(self,nhdf_rate=0.03):
        self.nhdf=self.gross_salary*nhdf_rate
        if self.nhdf>=2500:
            self.nhdf=2500
        else:
            self.nhdf=self.gross_salary*nhdf_rate


    def total_nhdf_nssf(self):
        self.total=self.nssf_contribution+self.nhdf

    def calculate_taxable_income(self):
        self.taxable_income=self.gross_salary-self.total


    def calculate_payee(self,personal_relief=2400):
        if self.taxable_income>=0 and self.taxable_income<=24000:
            gross_payee=24000*0.1
            self.net_payee=gross_payee-personal_relief
        elif self.taxable_income<=32333:
            gross_payee=(self.taxable_income-24000)*0.25+2400
            self.net_payee=gross_payee-personal_relief
        elif self.taxable_income<=500000:
            gross_payee=(self.taxable_income-32333)*0.3+4483.25
            self.net_payee=gross_payee-personal_relief
        elif self.taxable_income<=800000:
            gross_payee=(self.taxable_income-500000)*0.325+144783.35
            self.net_payee=gross_payee-personal_relief
        else :
            gross_payee=(self.taxable_income-800000)*0.35+242283.35
            self.net_payee=gross_payee-personal_relief


    def calculate_net_pay(self):
        self.net_pay=self.gross_salary-(self.total+self.net_payee+self.NHIF_contribution)

    def add(self):
        self.details["gross"]=self.gross_salary
        self.details["nssf"]=self.nssf_contribution
        self.details["nhdf"]=self.nhdf
        self.details["taxable_income"]=self.taxable_income
        self.details["NHIF"]=self.NHIF_contribution
        self.details["Payee"]=self.net_payee
        self.details["Net-pay"]=self.net_pay
        print(self.details)
            

p1=SalaryCalculator(input("enter basic salary: "),input("enter Benefits"))
print(p1.details
)


