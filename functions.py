import csv
import pandas as pd
import os
import string

def check_user_credentials(user_id,ic_number,password):
    """check if the user ID and Password are correct"""
    valid_user_id = 'danishimran2003'
    valid_ic_number = '030726100025'
    valid_password = '0025'

    if user_id != valid_user_id:
        print("Invalid user ID")
        return False
    if ic_number != valid_ic_number: 
        print("Invalid IC Number")
        return False
    if password != valid_password:
        print("Invalid Password")
        return False
    
    print("Login successful!")
    return True

def verify_user(ic_number, password):
    """Semak jika IC 12 digit dan password = 4 digit terakhir IC"""
    if len(ic_number) != 12 or not ic_number.isdigit():
        return False
    if password != ic_number[-4:]:
        return False
    return True

def calculate_tax(income, tax_relief):
    """Kira cukai berdasarkan income dan relief"""
    chargeable_income = income - tax_relief
    if chargeable_income <= 0:
        return 0  # Tiada cukai jika pendapatan bercukai <= 0
    
    # Contoh kadar cukai Malaysia (anggaran, boleh ubah ikut kadar sebenar)
    if chargeable_income <= 5000:
        tax = 0
    elif chargeable_income <= 20000:
        tax = (chargeable_income - 5000) * 0.01
    elif chargeable_income <= 35000:
        tax = (15000 * 0.01) + (chargeable_income - 20000) * 0.03
    elif chargeable_income <= 50000:
        tax = (15000 * 0.01) + (15000 * 0.03) + (chargeable_income - 35000) * 0.08
    else:
        tax = (15000 * 0.01) + (15000 * 0.03) + (15000 * 0.08) + (chargeable_income - 50000) * 0.14

    return tax

def save_to_csv(data, filename):
    """simpan data ke fail csv"""
    df_new = pd.DataFrame([data])

    if not os.path.isfile(filename):
        df_new.to_csv(filename, index=False)
    else:
        df_existing = pd.read_csv(filename)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        df_combined.to_csv(filename, index=False)

def read_from_csv(filename):
    """Baca data dari fail CSV dan pulangkan sebagai DataFrame"""
    if not os.path.isfile(filename):
        return None
    df = pd.read_csv(filename)
    return df
