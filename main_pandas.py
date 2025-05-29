import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json
import numpy as np
from datetime import datetime
import sys
import os
from tabulate import tabulate

salary_file = "salary_pandas.json"
data_file = r"C:\Users\Himanshu\OneDrive\Documents\my documents\python course\Python_Projects\FinanceTracker\data.json"
if os.path.exists(data_file) and os.path.getsize(data_file) > 0:
    df = pd.read_json(data_file)
else:
    df = pd.DataFrame()  # start with empty DataFrame



def load_to_salary(salary_file):
    try:
        with open(salary_file, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_to_data(data):
    with open(data_file, 'w') as file:
        json.dump(data, file, indent=4)

def load_to_data():
    try:
        with open(data_file, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

salary_data = load_to_salary(salary_file)

# This func is to log date while logging the transaction
def date():
    # This is  a list of months to show which month user has chosen
    months = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}
    # This func is used to get input in while selecting dates 
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
    # This func is for leap years
    def is_leap(year):
        return (year % 2 )
    # This func is to get day range according to the month and the year
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

    #this func is to let user selct a date whether be today or specific
    def logTime():
            print("--------------------------------------------")
            print("Enter the transaction_time here:\n1. today\n2. select specific transaction_time")
            transaction_time = int(input("-> (from 1 and 2)  "))
            # This is user wants to select todays date
            if transaction_time == 1:
                transaction_time = datetime.now().strftime("%d-%m-%Y[%H:%M]")
                print(f"Entered transaction_time is {transaction_time}")
                return transaction_time
            # This if user wants to select a specific date
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


def data_logging_system(transaction_time, amount, type, category):
    data = load_to_data()
    if not data:
        data = {
            'Dates' : [],
            "Amount" : [],
            "Type" : [],
            "Category" : [],
            "Remaining salary" : []
        }
    data['Dates'].append(transaction_time)
    data['Amount'].append(amount)
    data['Type'].append(type)
    data['Category'].append(category)
    data['Remaining salary'].append(salary_data['Remaining salary'])
    # This is to log in or add those transactions in the transaction.json file
    save_to_data(data)


def show_data(df):
    df = df[['Dates', 'Type', 'Category', 'Amount', 'Remaining salary']]
    print(tabulate(df, headers='keys', tablefmt='fancy_grid'))



# Categorizing expanses
def show_expanses():
    expanses = df.query('Type == "expanse"')
    expanses = expanses.groupby(['Type','Category'])['Amount'].sum().reset_index()
    print(tabulate(expanses, headers='keys', tablefmt='fancy_grid'))

    if len(expanses['Category']) > 5:
        sns.barplot(data=expanses, x='Category', y='Amount', hue='Category', palette='rocket')
        for idx in range(len(expanses['Category'])):
            amount = expanses['Amount'].iloc[idx]
            plt.text(idx, amount + 50, str(int(amount)), ha='center')
        plt.axhline(y=salary_data['Initial Salary'], color='red', linestyle='--', linewidth=2, label="Salary")
        plt.legend()
        max_amount = max(salary_data['Initial Salary'], salary_data['Remaining salary'])
        plt.yticks(np.arange(0, max_amount + 10000, 5000))
        plt.grid(True)
    else:
        plt.figure(figsize=(10,4))
        plt.subplot(1, 2, 1)  # (rows, cols, plot_no)
        sns.barplot(data=expanses, x='Category', y='Amount', hue='Category', palette='rocket')
        for idx in range(len(expanses['Category'])):
            amount = expanses['Amount'].iloc[idx]
            plt.text(idx, amount + 1000, str(int(amount)), ha='center')
        plt.axhline(y=salary_data['Initial Salary'], color='red', linestyle='--', linewidth=2, label="Salary")
        plt.axhline(y=salary_data['Remaining salary'], color='blue', linestyle='-.', linewidth=2, label="Remaining salary")
        plt.legend()
        max_amount = max(salary_data['Initial Salary'], salary_data['Remaining salary'])
        plt.yticks(np.arange(0, max_amount + 10000, 5000))

        plots = [expanse for expanse in expanses['Amount']]
        plots.append(salary_data['Remaining salary'])
        labels = [categories.title() for categories in expanses['Category']]
        labels.append("Remaining Salary")
        colors = sns.color_palette('Set2', len(plots)).as_hex()  
        plt.subplot(1, 2, 2)
        plt.pie(plots, labels=labels, autopct="%1.1f%%", colors=colors, wedgeprops={'edgecolor': 'black', 'linewidth': 1, 'linestyle': '--'})
        plt.tight_layout()
        plt.show()


# Categorizing incomes
def show_income():
    incomes = df.query('Type == "income"')
    incomes = incomes.groupby(['Type','Category'])['Amount'].sum().reset_index()
    print(tabulate(incomes, headers='keys', tablefmt='fancy_grid'))




# This func is to save the salary in the salary file
def save_to_salary(salary):
    with open(salary_file, 'w') as file:
        json.dump(salary, file, indent=4)

#This func is to manage remaining salary
def manage_salary(amount, type):
    if type.lower() == "expanse":
        if salary_data["Remaining salary"] != 0:
            salary_data["Remaining salary"] -= amount
        else:
            salary_data["Remaining salary"] = salary_data["Initial Salary"] - amount
    elif type.lower() == "income":
        if salary_data["Remaining salary"] != 0:
            salary_data['Remaining salary'] += amount
        else:
            salary_data['Remaining salary'] = salary_data["Initial Salary"] + amount
    else:
        return
    save_to_salary(salary_data)


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

                    manage_salary(amount, type)
                    data_logging_system(transaction_time, amount, type, category)

                elif user == 2:
                    show_data(df)

                elif user == 3:
                    show_expanses()

                elif user == 4:
                    show_income()

                elif user == 5:
                    open(data_file, 'w').close()
                    open(salary_file, 'w').close()

                    data = {
                        'Dates' : [],
                        "Amount" : [],
                        "Type" : [],
                        "Category" : [],
                        "Remaining salary" : []
                    }
                    save_to_data(data)
                    salary_data = {"Initial Salary": 0, "Remaining salary": 0}  # reset in-memory dict too
                    save_to_salary(salary_data)
                    print("History cleared!!")
                    sys.exit()

                elif user == 6:
                    print("Good bye!\nThanks for your time..\nhope you have a good day...")
                    sys.exit()

                else:
                    print("Please choose from given option!")

            except ValueError:
                print("Invalid input - please choose from valid options...")

if __name__=="__main__":
        while True:
            if salary_data['Initial Salary'] == 0:
                print("Please, Enter the salary first!")
                setSalary = int(input("Enter your salary -\n-> "))
                salary_data['Initial Salary'] = setSalary
                save_to_salary(salary_data)
                trackerExecution()
            else:
                trackerExecution()







