first_name="  joh.n"
last_name="   Do,e"
#1. clean and display full name
full_name = first_name + last_name
" ".join(full_name)
print(full_name.strip().replace(".","").replace(",","").replace("  ",""))
