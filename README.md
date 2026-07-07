# ATM Management System

## 📌 Project Overview

The ATM Management System is a simple Command User Interface (CUI) project developed using Python. This project simulates basic ATM functionalities such as balance inquiry, cash withdrawal, and cash deposit. Each customer has a unique account number that is used to access their account information.

The project is designed to demonstrate the concepts of:

* Python Programming
* Functions
* Conditional Statements
* Loops
* Exception Handling
* Dictionary Data Structure
* User Input Validation

---

## 🚀 Features

* Customer login using a unique account number.
* Check account balance.
* Deposit money into the account.
* Withdraw money from the account.
* Prevent withdrawal when the balance is insufficient.
* Handle invalid inputs using Exception Handling.
* Menu-driven Command Line Interface (CLI).

---

## 🛠️ Technologies Used

* **Programming Language:** Python 3
* **Interface:** Command Line Interface (CLI)
* **Concepts Used:** Exception Handling, Functions, Dictionaries, Loops

---

## 📂 Project Structure

```text
ATM-Management-System/
│
├── atm.py              # Main Python file
├── README.md           # Project documentation
```

---

## ⚙️ Functionalities

### 1. Check Balance

Displays the current balance available in the customer's account.

### 2. Deposit Money

Allows the customer to deposit money into their account.

### 3. Withdraw Money

Allows the customer to withdraw money from their account if sufficient balance is available.

### 4. Account Verification

Each customer has a unique account number. The system verifies the account number before performing any operation.

---

## 🔄 Workflow

1. Start the application.
2. Enter the account number.
3. If the account exists, the main menu is displayed.
4. Choose one of the following options:

   * Check Balance
   * Deposit Money
   * Withdraw Money
   * Exit
5. Perform the selected operation.
6. Return to the main menu until the user exits.

---

## 🧩 Exception Handling Implemented

The project uses Python's exception handling mechanism to manage errors gracefully.

Examples:

* Invalid account number.
* Entering characters instead of numbers.
* Depositing a negative amount.
* Withdrawing an amount greater than the available balance.
* Invalid menu choices.

Example:

```python
try:
    amount = float(input("Enter amount: "))
except ValueError:
    print("Please enter a valid number.")
```

---

## 📸 Sample Menu

```text
========== ATM MANAGEMENT SYSTEM ==========
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
===========================================
Enter your choice:
```

---

## 🎯 Learning Outcomes

After completing this project, you will understand:

* How to build a menu-driven Python application.
* How to implement Exception Handling.
* How to manage customer accounts using dictionaries.
* How to perform basic banking operations in Python.
* How to validate user inputs and handle runtime errors.

---

## 🔮 Future Enhancements

* PIN Authentication
* Money Transfer Between Accounts
* Transaction History
* Account Creation and Deletion
* File Handling for Data Storage
* Database Integration using MySQL or SQLite
* Mini Statement Generation

---

## 👨‍💻 Author

**Omkar Date**

* B.Sc. Computer Science
* Python Developer
* GitHub: https://github.com/Omkar4682
* LinkedIn: https://www.linkedin.com/in/omkar-date-04969435b

---

## 📜 License

This project is developed for educational and learning purposes only.
