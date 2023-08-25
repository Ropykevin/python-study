# Create a file called mydstask.py and attempt the below questions:
# my_ds = [23,"Jane", (560),["Lesson", "Maths", {"currency" : "KES"}], 987, (76,"John")]
# 1. Print KES
# 2. Print 560
# 3. Print Maths
# 4. In the dictionary with the key currency, add another key “amount” with value 90
# 5. Reverse 987 to 789 without using an inbuilt -method or Assigning 789 manually.
#      Hint: Strings can be reversed using [::]
# 6. Change the name “John” to “Jane” . 
my_ds = [23,"Jane", (560),["Lesson", "Maths", {"currency" : "KES"}], 987, (76,"John")]
# print(my_ds.values("KES"))
print(my_ds[3][2]["currency"])
# print(my_ds[1])
# print(my_ds[3]["Lesson"])
my_ds[3][2]["amount"] = 90
print(my_ds)
# {"currency": "KES", "amount": 90}
# num_str = str(987)
# reversed_num_str = num_str[::-1]
# reversed_num = int(reversed_num_str)
# my_ds[5] = (76, "Jane")
# [23, "Jane", (560), ["Lesson", "Maths", {"currency": "KES", "amount": 90}], 987, (76, "Jane")]
