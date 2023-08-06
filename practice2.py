#lab 3 (Task 1)
import datetime #importing datetime

def calculate_age(birth_date): # the 'calculate_age' function takes 'birth_date' as input & calculate the age based on the current date using the datetime function
    today = datetime.date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def main(): #in the 'main' function, we ask the user for their name&date of birth using the 'input' function 
    print("Welcome! Please enter your information:")
    name = input("Name: ")
    dob_str = input("Date of Birth (YYYY-MM-DD): ")


    try:
        dob = datetime.datetime.strptime(dob_str, '%Y-%m-%d').date() #use a while loop to continuously ask for the date of birth until the user enters a valid date in the format "YYYY-MM-DD". We do this using the datetime.datetime.strptime function, which parses the input string into a datetime object with the specified format.
        age = calculate_age(dob) # the age is then calcualted using using the calculate_age function, and the result is printed to the user.
        print(f"Hello {name}, you are {age} years old.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

if __name__ == "__main__":
     main()








    