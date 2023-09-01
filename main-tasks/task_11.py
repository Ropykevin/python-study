from datetime import datetime, date
def calculate_age(birthdate):
  birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
  today = date.today()
  age_in_years = today.year - birthdate.year
  age_in_months = (today.year - birthdate.year) * 12 + (today.month - birthdate.month)
  age_in_days = (today - birthdate).days
  return age_in_years, age_in_months, age_in_days
birthdate = input("Enter your date of birth (YYYY-MM-DD): ")
age_in_years, age_in_months, age_in_days = calculate_age(birthdate)
print("Your age is {} years, {} months, and {} days.".format(age_in_years, age_in_months, age_in_days))