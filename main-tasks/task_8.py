speed=int(input("enter the speed: "))
def check_speed(speed):
  if speed < 70:
    print("Ok")
  else:
    demerit_points = (speed - 70) // 5
    print("Points:", demerit_points)
    if demerit_points > 12:
      print("License suspended")

check_speed(speed)