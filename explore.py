
name = 'Aasawari'
print("I am : " +name )

age =31
age_as_string =str(age)
print("You are :" +age_as_string)

# Alternate method of printing age as an integer value
age =34
print(f"You are : {age}")

name= "Aasawari"
greetings = "How are you, {}?"
Aasawari_greetings = greetings.format(name)
print(Aasawari_greetings)

Hrushikesh_greetings = greetings.format("Hrushikesh")
print(Hrushikesh_greetings)

myself = "Aasawari"
new_name = input("Enter your name :")
print(f"Hello {new_name}.My name is {myself}")



#Program where for loop and continue is being used.
# If car status is faulty , the program will skip it and jump into the next status.
car =["OK", "OK","OK","OK","Faulty","OK"]
for status in car :
  if status == "Faulty":
    print("Found Faulty car.. Skipped!")
    continue
  print(f"This car is {status}")
  print("Go to the production for Selling..!")
