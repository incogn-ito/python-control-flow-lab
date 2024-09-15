# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

# def print_greeting():
#     python_is_fun = True
#     if python_is_fun:
#         print("python is fun")
#     # Your code goes here. Remember to indent!
#     python_is_fun = True
#     if python_is_fun:
#         print("Python is fun!")

# # Call the function
# print_greeting()

# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    # Your control flow logic goes here
    letter = input('Enter a letter "a-z or A-Z":').lower()

    if len(letter) != 1 or not letter.isalpha():
        print("Invalid input. Please enter one letter ")
        return
    vowels = "aeiou"
    if letter in vowels:
        print(f"The letter {letter} is a vowel")
    else:
        print(f"The letter {letter} is a consonant")
    
# Call the function
check_letter()

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    # Your control flow logic goes here
    age_input = input('Enter your age:')

    if not age_input.isnumeric() or int(age_input) < 0:
        print('Invalid entry. Please enter a positive  number for age.')
        return
    age = int(age_input)

    if age < 18:
        print('You are not yet old enough to vote')
    else:
        print('You are old enough to vote.')

# Call the function
check_voting_eligibility()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    # Your control flow logic goes here
    dog_age_input = input('Enter dog age:')

    if not dog_age_input.isnumeric() or int(dog_age_input) < 0:
        print('Invalid entry. Please enter a positive number for age.')
        return
    dog_age = int(dog_age_input)

    if dog_age == 0:
        print(f'The dog\'s age in dog years is 0')
    elif dog_age == 1:
        print(f'The dog\'s age in dog years is 10')
    elif dog_age == 2:
        print(f'The dog\'s age in dog years is 20')
    elif dog_age > 2:
        dog_years= (dog_age - 2) * 7 + 20
        print(f'The dog\'s age in dog years is {dog_years}')
    else:
        print('Invalid entry. Please enter a positive number for age.')

# Call the function
calculate_dog_years()


# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    # Your control flow logic goes here
    cold_input = input('Enter if it is cold (yes/no):').lower()
    rain_input = input('Enter if it is raining (yes/no):').lower()

    if cold_input not in ['yes', 'no'] or rain_input not in ['yes', 'no']:
        print('Invalid entry. Please enter yes or no.')
        return

    if cold_input and rain_input == 'yes':
        print ('Wear a waterproof coat')
    elif cold_input == 'yes' and rain_input == 'no':
        print ('Wear a warm coat')
    elif cold_input == 'no' and rain_input == 'yes':
        print ('Carry an umbrella') 
    elif cold_input == 'no' and rain_input == 'no':
        print ('Wear light clothing')

# Call the function
weather_advice()

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    # Your control flow logic goes here
    month_entry = input('Enter the month of the year (Jan-Dec):').lower()
    day_entry = input('Enter the day of the month (1-31):')

    if month_entry not in ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']:
        print('Invalid month entry. Please enter the first three letters of a month.')
        return
    if not day_entry.isdigit:
        print('Invalid entry. Please enter a number (1-31) for the day of the month.')
        return
    
    day = int(day_entry)

    if day < 1 or day > 31:
        print('Invalid entry. Please enter a number between 1 and 31.')

    if (month_entry == 'dec' and day >= 21) or month_entry in ['jan', 'feb'] or (month_entry == 'mar' and day <= 19):
        season = 'Winter'
    elif (month_entry == 'mar' and day >= 20) or month_entry in ['apr', 'may'] or (month_entry == 'jun' and day <= 20):
        season = 'Spring'
    elif (month_entry == 'jun' and day >= 21) or month_entry in ['jul', 'aug'] or (month_entry == 'sep' and day <= 21):
        season = 'Summer'
    elif (month_entry == 'sep' and day >= 22) or month_entry in ['oct', 'nov'] or (month_entry == 'dec' and day <= 20):
        season = 'Fall'

    formatted_month = month_entry.capitalize()

    print(f'{formatted_month} {day_entry} is in {season}')

# Call the function
determine_season()

# Exercise 7: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.

def guess_number():
    correct_number = 42
    max_attempts = 5

    # Your control flow logic goes here
    for attempt in range(1, max_attempts + 1):
        
        guess_input = input(f"Guess {attempt}: Guess a number between 1 and 100")
        
        if not guess_input.isnumeric() or int(guess_input) < 0 or int(guess_input) > 100:
            print("Invalid entry. Please guess a positive number between 1 and 100.")

        guess = int(guess_input)

        if guess == correct_number:
            print("Congrats! you guessed correctly!")
            break
        elif guess < correct_number:
            print("Guess is too low!")
        else: 
            print("Guess is too high!")
            
        if max_attempts == 5:
            print("Last chance!")
        else:
            print("Sorry, you failed to guess the number in 5 attempts")
    


# Call the function
guess_number()

