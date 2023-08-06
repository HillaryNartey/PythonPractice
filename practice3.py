#lab 4(Task 2)

#I added a 'get_age_category' function that takes the calculated age as input and returns the corresponding age category based on the given ranges. After calculating the age, the program determines the age category using this function and prints the result along with the age and the user's name.

import datetime

def calculate_age(birth_date):
    today = datetime.date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def get_age_category(age):
    if age <= 11:
        return "Kid"
    elif age <= 20:
        return "Adolescent"
    elif age <= 60:
        return "Adult"
    else:
        return "Old Person"

def main():
    print("Welcome to the Age Classifier!")
    name = input("Please enter your name: ")

    while True:
        try:
            birth_date_str = input("Please enter your date of birth (YYYY-MM-DD): ")
            birth_date = datetime.datetime.strptime(birth_date_str, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid date format. Please enter a valid date in the format YYYY-MM-DD.")

    age = calculate_age(birth_date)
    age_category = get_age_category(age)

    print(f"Hello, {name}! You are {age} years old, which makes you a {age_category}.")

if __name__ == "__main__":
    main()
