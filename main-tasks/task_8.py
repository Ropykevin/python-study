speed = int(input("Enter the speed: "))

def check_speed(speed):
    if speed < 70:
        return "Ok"
    else:
        demerit_points = (speed - 70) // 5
        if demerit_points > 12:
            return "License suspended"
        else:
            return "Points: " + str(demerit_points)

result = check_speed(speed)
print(result)
