import random
Ctemp=round(random.uniform(0,100),2)
Ftemp=round(random.uniform(32,212),2)
day=int(input("Enter the day :"))
month=int(input("Enter the month:"))
year=int(input("Enter the year:"))
if ((month>=1 and month<=12) and (day>=1 and day<=30) and (year>=1900 and year<=2024)):
    print(day,month,year,sep="/")
else:
    print("Invalid format of date ")   
User=input("Do you want to continue?(Yes/No):")
if (User.upper()=="YES"):
    print("Ok let's continue")
    Admin=input("Enter your name:")
    Age=int(input("Enter your age:"))
    if (Admin=="Rabindra Dhakal" and Age>=18):
           print(f"Welcome {Admin}, You have admin rights.")
    elif(Admin=="Mira Vorne" and Age>=18):
           print(f"Welcome {Admin}, you have super user rights.")    
    elif (Age>=18 and Admin!="Mira Vorne" and Admin!="Rabindra Dhakal" ):
            print(f"Welcome {Admin},you have viewer rights") 
            Temp=input("Enter the temperature format(C/F):")
            if (Temp.upper()=="C" and Ctemp>120):
              print(f"CPU TEMP is {Ctemp} C and ison fire")
            elif(Temp.upper()=="C" and (Ctemp> 100 and Ctemp<120) ):
               print(f"Cpu TEMP is {Ctemp} Cand too hot.")
            elif(Temp.upper()=="C" and (Ctemp<=100)):
               print(f"The Cpu temp is {Ctemp} C and is ok.")
            elif (Temp.upper()=="F" and Ftemp>220):
             print(f"The cpu TEMP IS {Ftemp} F and  is burning.")
            elif (Temp.upper()=="F" and (Ftemp>212 and Ftemp<220))  :
              print(f"Cpu Temperature is {Ftemp}F and  is  too hot ")  
            elif (Temp.upper()=="F" and (Ftemp<=212)):
               print(f"Temp is {Ftemp}F and  ok.")    
            Movement=random.choice(["Yes","No"])
            if(Movement.upper()=="Yes"):
                print("Movement detected")
            else:
                print("Movement not detected:")       
    else:
         print(f"Greetings {Admin}, you are too young to operate this program.")

else:
    print("Thanks for visiting us .")


