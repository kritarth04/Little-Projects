print("Enter Your Details")
name = input("Name: ")
ex = int(input("Experience (in years): "))
post = input("Enter your Designation:")
salary = int(input("Enter your salary : "))


if ex >= 5 and post == "manager":
    salary += (salary * 15/100)
    print (f"Your salary after bonus for this month is {salary}")
elif ex >= 5 :
    salary += (salary * 10/100)
    print (f"Your salary after bonus for this month is {salary}")
else:
    salary += (salary * 5/100)
    print (f"Your salary after bonus for this month is {salary}")