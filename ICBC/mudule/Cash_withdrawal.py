#_author:无言宝宝
#date:  2019/8/1

#Cash withdrawal:取现
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

def Cash_withdrawal():#{"1": {"0": "1", "1": "1", "2": "1", "3": "115000100001000520", "4": 10000}}
    f = open("../conf/Current_login_account.txt", "r")
    account_number=f.read()
    print("hello,\nAccount:%s \nYou are welcome to use ICBC cash withdrawal service."%(account_number))
    choose=input("How much would you like to withdraw?\n>>>").strip()#你想取多少钱
    payment_code=input("Please enter your payment password\n>>>").strip()#输入支付密码
    if choose.isdigit()==True:
        f = open("../conf/Account information.txt", "r")
        USinfo = json.loads(f.read())
        f.close()
        USpayment_code=USinfo[account_number]["2"] #支付密码
        USbalance=USinfo[account_number]["3"]  #账户余额
        choose=int(choose)
        USbalance = int(USbalance)
        if payment_code ==USpayment_code:#判断用户密码是不是对的
            if USbalance>=choose: #判断余额比要取的钱多
                f = open("../conf/Account information.txt", "w")
                difference=USbalance-choose
                USinfo[account_number]["3"] = difference
                data = json.dumps(USinfo)
                f.write(data)
                f.close()
                logger = Check_bank_card_statement.get_logger()
                logger.critical("Successful withdrawal!\nYou have withdrawn this time: %sYuan, your current balance is: %sYuan."%(choose,difference))
                print("Cash withdrawal successful!\nYour current balance is: %s"%(difference))
                choose=input("To continue withdrawing cash input T,\nReturn to main menu input Q\n>>>").strip()
                if choose=="T":
                    Cash_withdrawal()
                if choose=="Q":
                    The_main_interface.Feature_selection()
                elif choose != "T" and choose != "Q":
                    print("Your input is not compliant, please re-enter!")
                    Cash_withdrawal()

            elif USbalance<choose:
                print("Your balance is insufficient. \nYour balance is:%s"%(USbalance))
                choose=input("Enter T to Reprocessing withdrawal OR enter Q to return to the main menu.").strip()
                if choose=="T":
                    Cash_withdrawal()
                if choose=="Q":
                    The_main_interface.Feature_selection()

                elif choose != "T" and choose != "Q":
                    print("Your input is not compliant, please re-enter!")
                    Cash_withdrawal()

        elif payment_code !=USpayment_code:
            print("Your password is incorrect, please enter it again!\nPlease note that you are entering a payment password, not a login password!")
            Cash_withdrawal()

    elif choose.isdigit()==False or choose==None :
        print("Your input is not compliant, please re-enter!")
        Cash_withdrawal()

