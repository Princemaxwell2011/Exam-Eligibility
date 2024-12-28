print("Program to find Exam Eligibility")
score=float(input("Enter your Exam Eligibility "))

BMI=score/100**2
print("Your Exam Eligibility is:", BMI)

if BMI <= 39.4:
 print("Excellent")

elif BMI <= 29.9:
 print("Very good")

elif BMI <= 26.9:
 print("Good")

elif BMI <= 18.9:
 print("Poor")

else:
 print("Very poor.")
