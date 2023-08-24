#Remove friday and sunday from the set using methods.
#Add them back to the set

days={"monday","tuesday","wednesday","thursday","friday","saturday","sunday","sunday","saturday"}
days.remove("friday"),days.remove("sunday")
print(days)
days.add("friday"),days.add("sunday")