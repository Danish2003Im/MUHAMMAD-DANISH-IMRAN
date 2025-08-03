import pandas as pd
import os

from functions import verify_user, calculate_tax, save_to_csv, read_from_csv

USERS_FILE = 'users.txt'
CSV_FILE = 'tax_records.csv'

def register_user(user_id, ic_number):
    with open(USERS_FILE, 'a') as f:
        f.write(f'{user_id},{ic_number}\n')

def is_user_registered(user_id):
    if not os.path.isfile(USERS_FILE):
        return False
    with open(USERS_FILE, 'r') as f:
        for line in f:
            if line.strip().split(',')[0] == user_id:
                return True
    return False

def get_user_ic(user_id):
    with open(USERS_FILE, 'r') as f:
        for line in f:
            uid, ic = line.strip().split(',')
            if uid == user_id:
                return ic
    return None

def main():
    print("Welcome to Malaysian Tax Program!")

    user_choice = input("Are you a new user? (yes/no): ").strip().lower()

    if user_choice == 'yes':
        user_id = input("Please enter your new ID: ").strip()
        ic_number = input("Please enter your IC (12 digit): ").strip()
        password = input("Register password (last 4 digit of IC): ").strip()
        register_user(user_id, ic_number)
    elif user_choice == 'no':
        user_id = input("Please enter your ID: ").strip()
        ic_number = input("Please enter your IC (12 digit): ").strip()
        password = input("Please enter your Password (last 4 digits of IC): ").strip()
    else:
        print("Invalid choice. Exiting Program")
        return False

    if not verify_user(ic_number, password):
        print("Verification failed! Please check your IC and Password")
        return

    print("Your verification is successful! Please Log In")

    try:
        income = float(input("Enter your annual income (RM): "))
        tax_relief = float(input("Enter your tax relief amount (RM): "))
    except ValueError:
        print("Invalid number format")
        return

    tax_payable = calculate_tax(income, tax_relief)
    print(f"Your calculated tax payable is: RM {tax_payable:.2f}")

    user_data = {
        'User ID': user_id,
        'IC Number': ic_number,
        'Income': income,
        'Tax Relief': tax_relief,
        'Tax Payable': tax_payable
    }

    save_to_csv(user_data, CSV_FILE)

if __name__ == "__main__":
    main()

