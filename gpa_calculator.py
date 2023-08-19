number1 = int(input("Enter your mark for Bangla :"))
number2 = int(input("Enter your mark for English :"))
number3 = int(input("Enter your mark for Math :"))
number4 = int(input("Enter your mark for Science :"))


sum = number1 + number2 + number3 + number4

avarage = sum / 4

if 91 < avarage < 100:
    print("A+")
elif 81 < avarage < 90:
    print("A")
elif 71 < avarage < 80:
    print("B")
elif 61 < avarage < 70:
    print("C")
elif 41 < avarage < 60:
    print("D")
elif 0 < avarage < 40:
    print("F")
else:
    print()
