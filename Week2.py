import random
import string
def usernamegenerate(fname,lname,date):
    username=fname+lname+str(date)
    return username
def passwordgenerator(length,smallletters,capitalletters,specialletters,numbers):
    if smallletters+capitalletters+specialletters+numbers>length:
        print("Exceeded the password length ")
        return None
    
    password=(random.choices(string.ascii_lowercase,k=smallletters)+random.choices(string.ascii_uppercase,k=capitalletters)+random.choices(string.digits,k=numbers)+random.choices(string.punctuation,k=specialletters))
    random.shuffle(password)
    return "".join(password)
def check_birth_date(day, month, year):
    """Validates the birth date format."""
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return day <= 31
    elif month in {4, 6, 9, 11}:
        return day <= 30
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return day <= 29
        else:
            return day <= 28
    return False

def temperature(temp,temperature1):
    if temp.lower()=="c":
        if temperature1>120:
            print("It is hot and burning.")
        elif  temperature1>100:
            print("It is hot be careful.")    
        elif  50<temperature1<90:
            print("It is medium and but be cautious")    
        else:
            print("It is cool.")      
    elif temp.lower()=="f":
        if temperature1>=230:
            print("It is hot and burning.")
        elif 212 < temperature1 <= 230:
            print("It is hot be careful.")    
        elif  150 < temperature1 <= 200:
            print("It is medium and but be cautious")     
        elif 100 < temperature1 <= 130:
            print("It maybe slighlty hot but not so hot.")  
        else:
            print("It is cool.")     
    else:
         print("Invalid input")        
def main():  
    while True:  
        fname=input("Enter your firstname: ")
        lname=input("Enter your lastname: ")
        date=(input("Enter your birthyear(e.g.=2019): "))
        print(usernamegenerate(fname,lname,date))  
        day=int(input("Enter the day of your birthday: "))
        month=int(input("Enter the month of your burthday: "))
        year=int(input("Enter the year of your birthday: "))
        if not check_birth_date(day,month,year):
            print("Invalid bithdate format")
            continue
        print(f"Your dob is {year}/{month}/{day}")
        while True: 
            length=int(input("Enter the length of your desired password: "))
            smallletters=int(input("Enter the length of small characters: "))
            capitalletters=int(input("Enter the length of capital characters: "))
            specialletters=int(input("Enter the length of special characters: "))
            numbers=int(input("Enter the length of  numbers: "))
            password1=passwordgenerator(length,smallletters,capitalletters,specialletters,numbers)
            if password1:
                print(password1)
                # break
            else:
               continue    
        
            ask=input("Are you satisfied with your password(Yes/No?): ")
            if ask.lower()=="yes":
                break
            else:
                continue
    
        while True:    
            name=input("Enter your full name: ")
            age=int(input("Enter your age: "))
            if age<18:
              print("You are not eligible to execute the program.")
              continue

            elif  name=="Rabindra Dhakal" and age>=18:
                print(f"Greetings {name},you have admin rights.")
            elif name=="Mira Vorne" and age>=18:
                print(f"Greetings {name},you have super user rights.")    
            else:
                print(f"Greetings {name}, you have viewer rights.")  
            break 
        while True:
            print("Lets calculate the temperature.")
            temp=input("Enter the temperature in desired format(C or F): ")
            if temp.lower() == "c":
                temperature1 = round(random.uniform(0,120),2)
                print(f"temperature is {temperature1}  degree celsius")
                temperature(temp,temperature1)
                break
            elif temp.lower()== "f":
                temperature2 = round(random.uniform(32,230),2)
                print(f"temp is {temperature2} degree fahrenheit")
                temperature(temp,temperature2)
                break
        Movement=["Movement detected","Movement not detected"]
        move=random.choice(Movement)    
        print(move)
        while True:
            num2=random.randrange(1,100)
            attempt=0
            max_attempts=8
            while attempt < max_attempts:
                num=int(input("Enter a number between 1 and 100: "))
                print(f"Your number is {num}")
                attempt+=1
                if num>num2:
                    print("Your number is high")
                    
                elif num2>num:
                    print("Your number is low.")  
                    
                else:
                    print("Congratulations.Your number is matched.")
                    break  
            if attempt == max_attempts:
                print(f"You have no attempts remaining.Try next time.The number was {num2}")
            playagain=input("Do you want to play again(yes/no)?")
            if playagain.lower() != "yes":
                print("Thanks for visiting us .")     
                break

main()    


