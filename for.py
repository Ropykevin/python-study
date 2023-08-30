# write a for loop to print numbers from 1 to 5
numbers = range(0,5)
for number in numbers:
    print(number)

# sum all the elements in a list using a for loop numbers 
# numbers = [2, 3, 4, 5, 6, 7, 8, 9]
# total = []
# for number in range(1000):
#   total += number
# print(total)

number = list(range(0,51))
odd =[]
for i in number:
    if i%2>0:
        odd.append(i)
        if len(odd)==15:
            break
print(odd)
count= 0
for i in range(0,50):
    # if len(i)==10:
    if i%2>0:
        print(i)
        count =count+1
        if count==10:
         break
    else:
        pass



