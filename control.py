"""""
age = int(input("How old are you?: "))

if age >= 90:
        print(f"{age} is greater than 90")
elif age < 90 and age > -1:
        print(f"You are below 90 ")
else:
        print(f"You input {age} is minus, which is imposible")
"""""

"""""
day = input("Enter the day of the week?: ")

match day:
          case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
              print("Is week day")
          case "Sat" | "Sunday" :
                print("Is the weekend")
          case _:
                print("The day doesn't exist")
               
"""""

"""""
Loops:
          For - use to eterate over a list
          While

"""""

# # For loop
# people = ["Lincoln", "John","Peter"]
# print(type(people))


# for person in people:
#           print(person)

# word = "Hello"
# for char_word in word:
#         print(char_word)

# count = 0
# while count < 10:
#           print(count,end="")
#           count += 1

# number = 0

# for i in range(10):
#         number += 1
#         print(number)

# #While loop
# password = input("Provide your password?: ")
# while password != "1234":
#           print("Wrong password")
#           password = input("Provide your password?: ")

# print("The password is correct")


#Nested loop
# for i in range(8):
#           for j in range(i):
#                   print("*", end="")
#           print()
#Do while loop



# if 1 == 1:
#           print("This is true")
# elif 1 == 2:
#         print("This is false")
# else:
#         print("This is also false")

# number = "lll"
# match(number):
#           case "lll":
#                 print("The number is lll")
#           case "ll":
#                     print("ll")
#           case _:
#                 print("The number is not lll or ll")