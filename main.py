from datetime import datetime
import json
import sys

file_name = "transaction.json"
expanse_file = "expanse.json"
salary_file = "salary.json"

# This func is to log date while logging the transaction
def date():
    months = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}
    def get_int(prompt, min_value, max_value, message):
        while True:
            try:
                value = int(input(f"{prompt}\n-> "))
                if min_value <= value <= max_value:
                    print(message, f"{value}")
                    return value
                else:
                    print(f"please enter number between {min_value} and {max_value}")
                    continue
            except ValueError:
                print("Invalid input, please input a number!")

    def is_leap(year):
        return (year % 2 )
    
    def get_day(month, year):
        if month in [1,3,5,7,8,10,12]:
             return get_int("Enter the day here", 1, 31, "The day is" )
        elif month == 2:
            if is_leap(year):
                 return get_int("Enter the day here", 1, 29, "the day is")
            else:
                return get_int("Enter the day here", 1, 28, "The day is")
        else:
             return get_int("Enter the day here", 1, 30, "The day is")

    def logTime():
            print("--------------------------------------------")
            print("Enter the transaction_time here:\n1. today\n2. select specific transaction_time")
            transaction_time = int(input("-> (from 1 and 2)  "))
            if transaction_time == 1:
                transaction_time = datetime.now().strftime("%d-%m-%Y[%H:%M]")
                print(f"Entered transaction_time is {transaction_time}")
                return transaction_time

            elif transaction_time == 2:
                year = get_int("Enter the year here, eg. 2003 ", 2000, int(datetime.now().strftime("%Y")), "The year is ")
                month = get_int("Enter the month here, eg. 11 ", 1, 12, "The month is")
                print(f"you have selected {months[month]}")
                day = get_day(month, year)
                print(day)
                hour = get_int("Enter the hour here, eg. 23", 1, 24, "The hour is")
                minute = get_int("Enter the minute here, eg. 50", 1, 60, "The minute is")
                transaction_time = f"{year}-{month}-{day}[{hour}:{minute}]"
                print(f"Entered transaction_time is {transaction_time}")
                return transaction_time

            else:
                print("Invalid input - please enter from 1 and 2")

    return logTime()

#this func is to load file for transaction.json
def load_to_file():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

#this func is to save transactions in transaction.json file
def save_to_file(transactions):
    with open(file_name, 'w') as file:
        json.dump(transactions, file, indent=4)

def load_to_expanse():
    try:
        with open(expanse_file, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_to_expanse(expanse):
    with open(expanse_file, 'w') as file:
        json.dump(expanse, file, indent=4)
        
def load_to_salary():
    try:
        with open(salary_file, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_to_salary(salary):
    with open(salary_file, 'w') as file:
        json.dump(salary, file, indent=4)

def deduct_salary(amount, type):
    salary = load_to_salary()
    if type.lower() == "expanse":
        if "Remaining salary" in salary.keys():
            salary["Remaining salary"] -= amount
        else:
            salary["Remaining salary"] = salary["Initial Salary"] - amount
    elif type.lower() == "income":
        if "Remaining salary" in salary.keys():
            salary["Remaining salary"] = salary["Initial Salary"] + amount
        else:
            salary["Remaining salary"] += amount
    else:
        return
    save_to_salary(salary)
    
def loadExpanse(type, category, amount):
    expanse = load_to_expanse()
    if type.lower() == "expanse":
        if category in expanse.keys():
            expanse[category]  += amount
            
        else:
            expanse[category] = amount
        save_to_expanse(expanse)

    elif type.lower() == "income":
        pass

def transaction_logging_system(transaction_time, amount, type, category):
    notes_input = input("do you want to leave a note( y for yes else just press any key )\n-> ")
    if notes_input == "y":
        print("--------------------------------------------")
        note = input("leave a note: ")
        transaction_history = {
            "Amount" : amount,
            "Type" : type.title(),
            "Category" : category.title(),
            "Note" : note,  
        }
    else:
        print("Thanks for your time, hope you have a good time")
        transaction_history = {
                "Amount" : amount,
                "Type" : type.title(),
                "Category" : category.title(),
            }
        
    # This is to log in or add those transactions in the transaction.json file
    transactions = load_to_file()
    transactions[transaction_time] = transaction_history
    save_to_file(transactions)

def view_file():
    transactions = load_to_file()
    i = 0
    for date, history in transactions.items():
        i = i + 1
        if "Note" in history:
            print("-----------------------")
            print(f"{i}. {date}\n   Amount spend is {history['Amount']} for {history['Category']}\n   p.s - {history['Note']}")
        else:
            print("-----------------------")
            print(f"{i}. {date}\n   Amount spend is {history['Amount']} for {history['Category']}")
    
def show_expanse():
    print("These are your Expanses - ")
    expanse = load_to_expanse()
    i = 0
    for key, value in expanse.items():
        i = i+1
        print("--------------------------------------------")
        print(f"{i}. {key.title()} - {value} Rs")

def show_income():
    salary = load_to_salary()
    print("These are your Income info - ")
    for key, value in salary.items():
        print("--------------------------------------------")
        print(f"{key.title()} - {value} Rs")
    
def trackerExecution():     

            print("--------------------------------------------")
            print("""           
Welcome to Finance Tracker!
--------------------------------------------
1. Log a new transaction
2. View all transactions
3. View your expanses             
4. Show my income
5. Clear your history                  
6. Exit the program
                  
Please select an option by entering 1, 2, 3, 4, 5, or 6.
""", end=" ")
            try:
                user = int(input("-> "))
                if user == 1:
                    transaction_time = date()
                    try:
                        print("--------------------------------------------")
                        amount = int(input("Enter the amount here:\n-> "))
                        if amount > 0:
                            print(f"Entered amount is {amount}Rs")
                        else:
                            print("please enter a positive amount!")
                            sys.exit()
                    except ValueError:
                        print("Invalid input - please input a valid integer")
                        
                    print("--------------------------------------------")
                    type = input("enter the type here:\n-> (Expanse/Income) ")
                    if type in ["expanse", "income"]:
                        print(f"Entered type is {type.title()}")
                    else:
                        print("Please, choose from above options..")
                        sys.exit()

                    print("--------------------------------------------")
                    category = input("enter the category:\n-> ")
                    print(f"Entered category is {category.title()}")

                    transaction_logging_system(transaction_time, amount, type, category)
                    deduct_salary(amount, type)
                    loadExpanse(type, category, amount)

                elif user == 2:
                    view_file()

                elif user == 3:
                    show_expanse()

                elif user == 4:
                    show_income()
                
                elif user == 5:
                    open(file_name, 'w').close()
                    open(expanse_file, 'w').close()
                    open(salary_file, 'w').close()
                    salary = load_to_salary()
                    salary["Initial Salary"] = 0
                    save_to_salary(salary)
                    

                elif user == 6:
                    print("Good bye!\nThanks for your time..\nhope you have a good day...")

                else:
                    print("Please choose from given option!")
                    
            except ValueError:
                print("Invalid input - please choose from valid options...")

if __name__=="__main__":
    while True:
        salary = load_to_salary()
        if salary["Initial Salary"] == 0:
            print("Please, Enter the salary first!")
            setSalary = int(input("Enter your salary -\n-> "))
            salary["Initial Salary"] = setSalary
            save_to_salary(salary)
            trackerExecution()
        else:
            trackerExecution()