# Question 5. Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
#         Unit                                                     Price  
# First 100 units                                               no charge
# Next 100 units                                              Rs 5 per unit
# After 200 units                                             Rs 10 per unit
# (For example if input unit is 350 than total bill amount is Rs2000)

units = int(input("enter the units of electricity used"))

if units <= 100:

    print("no charge because units used is too law")

elif units <=200:

    print("you have to pay Rs",units*5)

elif units >= 200:

    print("you have to pay Rs",units*10)

else:
    
    print("Ab office me aana saara bill ache se pay karva lenge bahoot pesa aa ra he office me de ke ja chup chap")
