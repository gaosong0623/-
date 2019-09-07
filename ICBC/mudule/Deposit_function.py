#_author:无言宝宝
#date:  2019/8/1

#存钱功能：

import json
import os
import sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from mudule import The_main_interface
from mudule import Check_bank_card_statement

def loading():
    import time
    for i in range(101):
        print('\r'+'>'*i,'%d%%'%i,end='')
        time.sleep(0.1)



def deposit():
    f = open("../conf/Current_login_account.txt", "r")
    account_number = f.read()
    f.close()
    f = open('../conf/Account information.txt',"r")
    data = json.loads(f.read())
    f.close()
    name = data[account_number]["0"]
    Balance = data[account_number]["3"]
    Credit_card_limit = data[account_number]["4"]
    Formatted_query_balance = """
        ========================================================

        Hello,%s,
        Your balance is:%s
        Your credit card limit is:%s

        ========================================================
        """ % (name, Balance, Credit_card_limit)
    print(Formatted_query_balance)
    select=input("Do you want to deposit? Confirm, press Y, cancel, press Q\n>>>").strip()
    if select=="Y":
        Save_money=input("How much would you like to deposit?\n>>>").strip()
        if Save_money.isdigit()==True:
            print("Please put in your cash...") #请放入现金
            select = input("Please enter Y after the banknote is finished.\n>>>").strip()  # 放入钞票后输入Y，取消输入Q
            if select == "Y":  # 放钞完毕
                print("Just a moment, please. We are checking your bill...")  # 正在检测钞票
                loading()
                Balance=int(Balance)
                Save_money=int(Save_money)
                Balance=Balance+Save_money
                f = open("../conf/Account information.txt", "r")
                USinfo = json.loads(f.read())
                f.close()
                f = open("../conf/Account information.txt", "w")
                USinfo[account_number]["3"] = Balance
                data = json.dumps(USinfo)
                f.write(data)
                f.close()
                logger = Check_bank_card_statement.get_logger()
                logger.critical("\nDeposit successfully!Your balance is %s + %s Amount"% (Balance, Credit_card_limit))  # 存款成功，你的余额是")
                print("\nDeposit successfully!Your balance is %s + %s Amount"% (Balance, Credit_card_limit))  # 存款成功，你的余额是
                select=input("Press Y to return to the main menu, or press Q to exit the program.\n>>>").strip()
                if select=="Y":
                    The_main_interface.Feature_selection()
                if select=="Q":
                    exit("Thank you for using ICBC,"
                        "We will make better optimization for you and wish you a happy life!")
                elif select != "Y" and select != "Q" :
                    print("Your input is not compliant, please operate again!")
                    deposit()

            elif select !="Y":
                print("Your input is not compliant, please operate again!")
                deposit()


        elif Save_money.isdigit()==False:
            print("You can only enter a numeric amount!")
            deposit()

    if select=="Q":
            print("Your operation has been canceled and is jumping for you, please wait...")
            The_main_interface.Feature_selection

    elif select!="Q" and select!="Y":
        print("Your input is not compliant, please re-enter!")
        deposit()