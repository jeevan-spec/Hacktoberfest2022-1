#Program to check wether entered passcode is correct . [3 times]
for i in range(1,4):
  x=input("Enter the password: ")
  if x!='SECRET':
    print("Password is incorrect.")
    print("You cannot enter.")
  else:
    print ("Password is correct.")
    print("You can enter.")
    break
