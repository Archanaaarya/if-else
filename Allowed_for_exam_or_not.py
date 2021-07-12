# Question 1. A student will not be allowed to sit in an exam if his/her attendance is less than 75%.Take following input from the user. Number of classes held. Number of classes attended. And print, percentage of class attended. Is the student is allowed to sit in the exam or not.

total_classes_held = int(input("enter the number of classes held"))

total_classes_attended =  int(input("enter the number of classes attended by student"))

percentage = (total_classes_attended/total_classes_held*100)

if percentage>=75:

    print(percentage, "student can be sit in examination")

else:
    
    print(percentage, "student can not be sit in examination")