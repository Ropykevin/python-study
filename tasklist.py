# trainees = ["John", [2, ["James","Mary"]]]

# 1. Display 2 using index, from the list.
# 2. Output James  using index, from the list.
# 3. Using a method add 56 at the end of the list.
# 4. Using a method add the name Mike between James and Mary
# 5. Change the value of 2 to 8
# 6. Remove John and Mary from the list.
# 7. Using a function, determine the length of the list
trainees = ["John", [2, ["James", "Mary"]]]
# 1. Display 2 using index, from the list.
print(trainees[1][0])  
# 2. Output James using index, from the list.
print(trainees[1][1][0])
# 3. Using a method add 56 at the end of the list.
trainees.append(56)
print(trainees)
# # 4. Using a method add the name Mike between James and Mary.
print(trainees[1][1].insert(1, "Mike"))
# # 5. Change the value of 2 to 8.
trainees[1][0] = 8
print(trainees)
# # 6. Remove John and Mary from the list.
trainees.remove("John")
del trainees[1][1][2]
print(trainees)
# # 7. Using a function, determine the length of the list.
length = len(trainees)
print(length)

name =["ke","uh","3"]
gam=["uk","za","tz"]
nm=["uk","ty","rt"]
name.extend(gam),name.extend(nm)
print(name)
