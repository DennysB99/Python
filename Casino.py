#
# CGS 2060 – Spring Semester 2024
#
# CGS 2060 Homework #1 – Welcome To The Casino
#
# Dr. Jim Anderson
#
# Student Name: Dennys Bach
#
# Initialize variables that will be used in program

badPerson1FirstName = "NORA"
badPerson1LastName  = "JONES"
badPerson2FirstName = "KENT"
badPerson2LastName  = "PERKINS"

vipPerson1FirstName = "CAROL"
vipPerson1LastName  = "TURNER"
#vipPerson1Level = "Silver"
vipPerson2FirstName = "MICHELLE"
vipPerson2LastName  = "UNSER"
#vipPerson2Level = "Gold"
vipPerson3FirstName = "PAMELA"
vipPerson3LastName  = "MUELLER"
#vipPerson3Level = "Platinum"

Platinum = [vipPerson3FirstName, vipPerson3LastName]
Gold = [vipPerson2FirstName, vipPerson2LastName]
Silver = [vipPerson1FirstName, vipPerson1LastName]

BadList = [badPerson1FirstName, badPerson1LastName, badPerson2FirstName, badPerson2LastName]
# Display welcome banner
print("Welcome to the CGS 2060 Casino!")
print()

# Calculate if the guest is old enough to enter the casino
Age = input("Please enter the age of the customer: ")

# Check to see if the guest is at least 21 years old
if int(Age) > 21:
  FirstName = input("Please enter your first name: ").upper()
  LastName = input("Please enter your last name: ").upper()
  # Check to see if guest is on the forbidden list
  if FirstName and LastName not in BadList:

    # Guest is at least 21 and is NOT on the forbidden list

    # Check for VIP #1 casino member
    if FirstName and LastName in Platinum:
      print(f"Welcome to the Casino {FirstName} {LastName}")
      print("Its a pleasure to see you today! I see you are a Platinum member!")
      print("Here are the 75 tokens.")

    # Check for VIP #2 casino member
    elif FirstName and LastName in Gold:
      print(f"Welcome to the Casino {FirstName} {LastName}")
      print("I see you are a Gold Member, Welcome back! Here are your 50 tokens.")

    # Check for VIP #3 casino member
    elif FirstName and LastName in Silver:
      print(f"Welcome to the Casino {FirstName} {LastName}")
      print("Good Luck today! Here are your 25 tokens.")

    else:
      print("Your good to go")

  else:
    print("Apologies, but you may not enter.")
# Guest is not 21
else:
  print("You are not old enough, GoodBye!")
  exit
