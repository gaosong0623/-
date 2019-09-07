#_author:无言宝宝
#date:  2019/8/5


import os
import sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from mudule import login
from mudule import Query_balance
from mudule import Deposit_function
from mudule import Cash_withdrawal
from mudule import transfer_accounts
from mudule import Check_bank_card_statement
from mudule import Shopping_mall


account_number=""
flag=""


def home():
    end1="""
     ========================================================
     Hello, welcome ICBC Credit card steward,
     We provide you with the following features:
     1.balance enquiry(查询余额）
     2.deposit(存款）
     3.Cash withdrawal(取现)
     4.transfer accounts(转账)
     5.Check bank card statement(查询账单）
     6.online shopping mall(网上商城)
     Stay tuned for more features……

     Please enter the corresponding serial number to visit,
     Press Q to exit,
     Enter T to log out the current login account
     ========================================================
     """
    print(end1)



def Feature_selection():
    home()
    user_selection=input(">>>").strip()
    if user_selection.isdigit()==True and user_selection<="6": #判断是否输入的是数字并且小于等于5
        f = open(r"..\conf\logging status.txt", "r")
        logging_status = f.read()
        f.close()
        if logging_status == "Not logged in":
            print("After logging in, you can enter the interface,"
                  " is jumping to login screen for you……")
            login.logger()

        if logging_status=="logged in":
            print("You are already logged in and are jumping to the function interface for you...")
            if user_selection == "1":
                Query_balance.balance_enquiry()
            if user_selection == "2":
                Deposit_function.deposit()
            if user_selection == "3":
                Cash_withdrawal.Cash_withdrawal()
            if user_selection == "4":
                transfer_accounts.transfer()
            if user_selection == "5":
                Check_bank_card_statement.bill()
            if user_selection == "6":
                Shopping_mall.Shopping()

    if user_selection=="Q":
        exit("Thank you for using ICBC,"
            "We will make better optimization for you and wish you a happy life!")

    if user_selection == "T":
        f = open(r"..\conf\logging status.txt", "r")
        logging_status = f.read()
        f.close()
        if logging_status=="Not logged in":
            print("You are not logged in, you cannot log out!")
            Feature_selection()

        if logging_status=="logged in":
            f = open(r"..\conf\logging status.txt", "w")
            f.write("Not logged in")
            f.close()
            f = open(r"..\conf\Current_login_account.txt", "w")
            f.truncate()
            f.close()
            print("You have successfully logged out and are returning to the main menu for you...")
            Feature_selection()

    elif user_selection !="Q" and user_selection !="T" or user_selection.isdigit()==True and user_selection>"6":
        print("Please enter standard options!")
        Feature_selection()



