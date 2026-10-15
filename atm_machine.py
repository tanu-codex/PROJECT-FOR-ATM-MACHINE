
import openpyxl
import os
FILE_NAME = "ATM_Accounts.xlsx"
# 1. CREATE ACCOUNT 
def create_account():
    account_number = int(input("Enter Account Number:"))
    name = input("Enter Account Holder Name:")
    address = input("Enter Contact Number:")
    balance = float(input("Enter Current Balance:"))
    if os.path.exists(FILE_NAME):
        workbook = openpyxl.load_workbook(FILE_NAME)
        sheet = workbook.active
    else:
        workbook = openpyxl.Workbook()
        sheet = workbook.active

        sheet.append([
        "Account Number",
        "Account Holder Name",
        "Address",
        "Contact Number",
        "Balance"
        ])

    sheet.append([
        account_number,
        name,
        address,
        contact,
        balance
    ])

    workbook.save(FILE_NAME)

    print("Your account is created successfully!")
    print("Your Account Number is:", account_number)


# 2. DEPOSIT MONEY 
def deposite_money():
    account_number = int(input("Enter Account Number: "))
    amount = float(input("Enter deposited money: "))

    workbook = openpyxl.load_workbook(FILE_NAME)
    sheet = workbook.active

    found = False

    for row in range(2,sheet.max_row + 1):

        if sheet.cell(row, 5).value == account_number:
            current_balance = sheet.cell(row, 5).value
            new_balance = current_balance + ammount
            sheet.cell(row, 5).value = new_balance
            workbook.save(FILE_NAME)

            print("Your money has been deposited successfully!")
            print("Current Balance:", new_balance)

            found = True
            break
    

    if found == False:
       print("Account not found.")

# 3. WITHDRAW MONEY
def withdraw_money():
    account_number = int(input("Enter Account Number:"))
    amount = float(input("Enter amount to withdraw:"))

    workbook = openpyxl.load_workbook(FILE_NAME)
    sheet = workbook.active

    found = False

    for row in range(2, sheet.max_row + 1):

        if sheet.cell(row, 1).value == account_number:

            current_balance = sheet.cell(row, 5).value

            if amount > current_balance:
                print("Your account does not have enough money.")

            else:
                new_balance = current_balance - amount 
                sheet.cell(row, 5).value = new_balance
                workbook.save(FILE_NAME)

                print("Amount successfully withdrawn.")
                print("Current Balance:", new_balance)

            Found = True
            break

        if found == False:
            print("Account not found.")


# 4. SHOW BALANCE 
def show_balance():
    account_number = int(input("Enter Account Number: "))

    workbook = openpyxl.load_workbook(FILE_NAME)
    sheet = workbook.active

    found = False

    for row in range(2, sheet.max_row + 1):

        if sheet.cell(row, 1).value == account_number:

            balance = sheet.cell(row, 5).value

            print("Account Holder:", sheet.cell(row, 2).value)
            print("Current balance:", balance)

            found = True
            break

    if found == False:
        print("Account not found.")


# ATM MENU
def menu():
    print("\n========================")
    print("        ATM SYSTEM")
    print("========================")
    print("1. Creat Account")
    print("2. Deposite Money")
    print("3. withdraw Money") 
    print("4. Show Balance")
    print("5. Exit")
    print("========================")

# MAIN PROGRAM 
while True:

    menu()
    ch = int(input("Enter your choice:"))
    if ch == 1:
        create_account()

    elif ch == 2:
        if os.path.exists(FILE_NAME):
            deposite_money()
        else:
            print("Please create an account first.")

    elif ch == 3:
        if os.path.exists(FILE_NAME):
            withdraw_money()
        else:
            print("Please create an account first.")

    elif ch == 4:
        if os.path.exists(FILE_NAME):
            show_balance()
        else:
            print("Please create an account first.")

    elif ch == 5:
         print("Thank you for using ATM System!")
         break
    
    else:
          print("Enter a valid choice.") 
