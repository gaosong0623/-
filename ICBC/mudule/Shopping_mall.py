#_author:无言宝宝
#date:  2019/8/1


import os
import sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from mudule import The_main_interface
from mudule import Check_bank_card_statement
import json



def style():
    global name1, price1, name2, price2, name3, price3, name4, price4, name5, price5,data

    name1 = data[0]["name"]
    name2 = data[1]["name"]
    name3 = data[2]["name"]
    name4 = data[3]["name"]
    name5 = data[4]["name"]
    price1 = data[0]["money"]
    price2 = data[1]["money"]
    price3 = data[2]["money"]
    price4 = data[3]["money"]
    price5 = data[4]["money"]
    buy()



def buy():
    end2="""
===============================
If you want to buy, 
please enter the corresponding serial number.    
To view other product categories, enter T
===============================   
"""
    global name1, price1, name2, price2, name3, price3, name4, price4, name5, price5
    end1 = """
    ===============================
    1.%s：%s元
    2.%s：%s元
    3.%s：%s元
    4.%s：%s元
    5.%s：%s元
    ……更多商品敬请期待
    ===============================
    """ % (name1, price1, name2, price2, name3, price3, name4, price4, name5, price5)
    print(end1)
    print(end2)
    choose=input(">>>").strip()
    if choose=="T":
        Shopping()

    if choose.isdigit()==True and choose<="5":
        if choose=="1":
            name=name1
            money=price1
        if choose == "2":
            name = name2
            money = price2
        if choose == "3":
            name = name3
            money = price3
        if choose == "4":
            name = name4
            money = price4
        if choose == "5":
            name = name5
            money = price5

        print("Are you sure you want to buy:%s,Amount:%s?"%(name,money))
        select=input("Ok, enter Y,\nCancel operation by entering Q\n>>>")
        if select=="Y":#确定要购买
            payment_code=input("Please enter your payment password\n>>>").strip() #输入支付密码
            f = open("../conf/Current_login_account.txt", "r") #取当前登录的账户名
            account_number = f.read() #账户名
            f.close()
            f = open("../conf/Account information.txt", "r") #打开账户信息文件
            USinfo = json.loads(f.read())
            f.close()
            USpayment_code = USinfo[account_number]["2"]  # 支付密码
            USbalance = USinfo[account_number]["3"]  # 账户余额
            if USpayment_code==payment_code: #如果账户密码==用户输入的密码
                if USbalance>=money: #如果账户余额比商品价格多：
                    f = open("../conf/Account information.txt", "w")
                    USbalance=USbalance-money
                    USinfo[account_number]["3"]=USbalance
                    USinfo=json.dumps(USinfo)
                    f.write(USinfo)
                    f.close()
                    logger = Check_bank_card_statement.get_logger()
                    logger.critical("Purchase success! You purchased:%s, the amount is:%s, your current balance is:%s."%(name,money,USbalance))
                    print("Purchase success!")
                    buy()
                elif True:
                    print("Your balance is insufficient to purchase...")
                    buy()

            elif True:#如果支付密码不对
                print("Your password is incorrect, please enter it again!\nPlease note that you are entering a payment password, not a login password!")
                buy()

        if select=="Q":#取消购买
            print("The operation has been cancelled for you, jump to the interface...")
            Shopping()

        elif True:
            print("Your input is not compliant, please re-enter!")


    elif True:
        print("Your input is not compliant, please re-enter!")
        buy()



def Shopping():
    end1="""
=========================================================== 
   
Welcome to shopping mall function,
We offer you the following kinds of goods:
1.Fresh fruit(水果生鲜)
2.Intelligent technology products(科技产品)
3.snacks(零食)
……More varieties are being added……

For more information,
please enter the number before the product category.
To return to the main menu, enter T,
To exit the program, enter Q.
===========================================================  
    """
    f = open("../conf/list.py", "r",encoding="utf-8")
    global data
    data = eval(f.read())
    f.close()

    print(end1)
    global choose
    choose = input(">>>")


    if choose == "1":
        data=data["1"]
        style()

    if choose == "2":
        data=data["2"]
        style()
    if choose == "3":
        data=data["3"]
        style()

    if choose == "T":
        The_main_interface.Feature_selection()

    if choose == "Q":
        exit("Thank you for using ICBC,\nWe will make better optimization for you and wish you a happy life!")

    elif choose!="1" and choose!="2" and choose!="3":
        print("Please enter the corresponding serial number!")
        Shopping()

