import time
import json
import sys

file_name = "transaction.json"

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
                transaction_time = time.strftime("%d-%m-%Y[%H:%M]")
                print(f"Entered transaction_time is {transaction_time}")

            elif transaction_time == 2:
                year = get_int("Enter the year here, eg. 2003 ", 2000, int(time.strftime("%Y")), "The year is ")
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

def transaction_logging_system():
    def load_to_file():
        try:
            with open(file_name, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_to_file(transactions):
        with open(file_name, 'w') as file:
            json.dump(transactions, file, indent=4)

    def log_in_transaction():
        while True:
            transaction_time = date()
            try:
                amount = int(input("Enter the amount here:\n-> "))
                if amount > 0:
                    print(f"Entered amount is {amount}Rs")
                else:
                    print("please enter a positive amount!")
                    continue
            except ValueError:
                print("Invalid input - please input a valid integer")
                
            type = input("enter the type here:\n-> (Expanse/Salary) ")
            print(f"Entered type is {type.title()}")

            category = input("enter the category:\n-> ")
            print(f"Entered category is {category.title()}")

            notes_input = input("do you want to leave a note( y for yes else just press any key )\n-> ")
            if notes_input == "y":
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

            transactions = load_to_file()
            transactions[transaction_time] = transaction_history
            save_to_file(transactions)

    log_in_transaction()


if __name__=="__main__":
    transaction_logging_system()