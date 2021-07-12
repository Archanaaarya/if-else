# Question 8. write a programm to check whether a number is divisable by 5 and 11 or not.

number = int(input("Enter the any number"))

if number % 5 == 0 and number % 11 == 0:

    print(number , ":this number is divisable by 5 and 11")

elif number % 5:

    print(number , ":This numebr is only divisable by 5")

elif number % 11:

    print(number , ":This number is divisable by only 11")

else:
    
    print(number , ":This number is not divisable by 5 or 11")