# project1-Expense-Tracker

# Expense Tracker (Basic Python Project)
## Project Overview
This project is a simple **Expense Tracker** built using Python.
It allows users to record daily expenses, view them, and calculate the total spending.
All data is stored in a file (`expenses.txt`), making it useful for learning **file handling and data storage**.

##  Features
* Add new expenses with description and date
* View all saved expenses
* Calculate total expenses
* Store data permanently using file handling
* Handle errors (invalid input, missing file)

##  Technologies Used
* Python
* File Handling
* `datetime` module



## How the Program Works

### 1️.Add Expense

* User enters:

  * Amount
  * Description
* Current date is automatically added
* Data is saved in `expenses.txt`

Example:

```id="3ynf99"
250 Food 19-03-2026
```

### 2️.Show Expenses

* Reads data from file
* Displays all recorded expenses

### 3️. Show Total

* Reads all expenses from file
* Calculates total spending

### 4️.Exit

* Ends the program

##  How to Run
1. Install Python
2. Save the file as `expense_tracker.py`
3. Run the program:

```bash id="0a9dnr"
python expense_tracker.py
```

##  Concepts Used

This project demonstrates:

* File handling (`read`, `write`, `append`)
* Exception handling (`try-except`)
* Loops and conditions
* String manipulation
* Date handling using `datetime`

##  Learning Outcomes

After completing this project, you will learn:

* How to store and retrieve data using files
* How to build real-world applications like expense trackers
* How to handle errors in user input
* How to work with dates in Python
* How to design menu-driven programs

## Possible Improvements

* Add category (Food, Travel, etc.)
* Monthly expense summary
* Delete or edit expenses
* Export data to CSV
* Build GUI using Tkinter
* Create web version using Flask

## Author

Harsha G
Learning **Python | Embedded Systems | IoT**
