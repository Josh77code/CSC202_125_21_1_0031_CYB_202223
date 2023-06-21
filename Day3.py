# Odd or even numbers 
number = int(input("Which number do you want to choose?"))
if number % 2 == 0:
    print("This is a even number")
else:
    print("This is an odd")
#Leap year Exercise 
year = int(input("Which year do you want to check?"))
if year % 4 ==0:
  if year % 100 ==0:
     if year % 400 ==0:
        print("Leap yaer")
     else:
        print("Not leap year")
  else:
     print("Leap year")
else:
   print("Not leap year")
#Pizzza order Exercise

print("Welcome to python pizza deliveries")
size = input("What size of pizza do you want? S, M,or L")
add_pepperoni = input("Do you want pepperoni? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N")
bill = 0

if size == "S":
   bill += 15
elif size == "M":
   bill += 20
else:
   bill += 25

if add_pepperoni == "Y":
   if size == "S":
      bill += 2
   else:
      bill += 3

if extra_cheese == "Y":
   bill += 1

print(f"Your final bill is ${bill}")

#Love calculator 

name1 = input("What is your name? \n")
name2 = input("What is thier name? \n")

combine_string = name1 + name2
lower_case_string = combine_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
true = t + r+ u +e 

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = str(true) + str(love)

print(love_score)

if (love_score < 10) or (love_score > 90):
   print(f"Your love score is {love_score}, you go like coke")
elif(love_score >= 40) and (love_score <= 50):
   print(f"your score is {love_score}, you are alright together")
else:
   print (f"your score is {love_score}"
          )





      
   

