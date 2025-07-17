print("enter marks obtained in 5 subject: ")
mark1 = int(input("enter the first subject"))
mark2 = int(input("enter the second sunject"))
mark3 = int(input("enter the third subject"))
mark4 = int(input("enter the fourth subject"))
mark5 = int(input("enter the fifth subject"))
sum = mark1 + mark2 + mark3 + mark4 + mark5;
average = sum/5;
if(average>=91 and average<=100):
    print("your grade is A+");
elif(average>=81 and average<=90):
    print("your grade is A");
elif(average>=71 and average<=80):
    print("your grade is B+");
elif(average>=61 and average<=70):
    print("your grade is B");
elif(average>=51 and average<=60):
    print("your grade is C+");
elif(average>=41 and average<=50):
    print("your grade is C");
elif(average>=0 and average<=40):
    print("your grade is F");
else:
    print("strange grade..!!");
