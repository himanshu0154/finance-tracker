# 💸 Finance Tracker (v2)

A command-line finance manager built with Python, Pandas, NumPy, Matplotlib, and Seaborn. Track your income, expenses, salary, visualize your spending habits, and maintain transaction logs — all in one smart terminal app.

# 🚀 Features

✅ Core Functionalities

- Transaction Logging: Log income or expenses with category, type, and timestamp.

- Salary Management: Set and update salary with automatic deduction/addition based on transaction type.

- Persistent Storage: All data is stored in data.json and salary_pandas.json files for persistence between runs.

- Date Selection: Choose between current date or select a custom transaction date and time.

# 📊 Visualizations

- Bar Graphs for categorized expenses and income.

- Pie Charts for quick proportion-based understanding of where your money goes.

- Salary Comparison Lines: Overlay your income vs salary vs remaining balance using Matplotlib.

# 📁 Data Storage Structure

- data.json
    Stores all transaction records including:

    - Dates

    - Amount

    - Type (income/expanse)

    - Category

    - Remaining salary after each transaction

- salary_pandas.json
    Stores initial and current salary to ensure financial tracking consistency.

# 🧠 Tech Stack

- pandas – Efficient data manipulation.

- numpy – Numeric handling for salary operations and plotting ranges.

- seaborn + matplotlib – Beautiful, insightful visualizations.

- tabulate – Clean CLI tables.

- json – Simple persistent data storage.

- datetime – Smart date handling.

# 🛠️ Setup Instructions

Prerequisites
Ensure Python 3.9+ is installed with the following libraries:

```bash
pip install pandas numpy matplotlib seaborn tabulate
```

## Running the App

1. Save your script as finance_tracker.py

2. Just run it:

```bash
python finance_tracker.py
```

## 🔐 How It Works

```bash
- On first run, you’ll be prompted to enter your salary.
- Then choose what you want to do:
    1. Log a new transaction
    2. View all transactions (tabular)
    3. View categorized expenses with visual breakdowns
    4. View categorized income
    5. Clear history and reset all data
    6. Exit
```

# 📦 Sample Data Format

## salary_pandas.json

```bash
{
  "Initial Salary": 50000,
  "Remaining salary": 33000
}
```

## data.json

```bash
{
  "Dates": ["2025-05-29[14:30]", "2025-05-29[15:00]"],
  "Amount": [2000, 500],
  "Type": ["income", "expanse"],
  "Category": ["freelance", "groceries"],
  "Remaining salary": [52000, 51500]
}
```

# 🤓 Cool Internals

- Custom Date Picker with leap year handling.

- Bar + Pie Chart Combo View: Automatically switches layout if expenses are fewer than 5 categories.

- Dynamic Tick Intervals on Y-axis based on your salary size.

- DataFrame manipulation for querying and grouping expenses and incomes by category.

- Separation of logic and storage for better maintainability.

# ❗ Known Limitations / To-Do

- No error handling for corrupted JSON files.

- No undo feature for logged transactions.

- CLI-only; no GUI (yet 😉).

- Basic input validation (but could use regex or stricter enforcement).

# 🧠 What I Learned

This project helped me:

- Apply real-world use of Pandas and NumPy for data processing.

- Use Matplotlib and Seaborn to make financial data intuitive.

- Handle file I/O, JSON storage, and build a full command-line interface.

- Understand how to work with time-based data using datetime.

# 🙌 Credits

Created with curiosity and caffeine by Himanshu ☕👨‍💻

