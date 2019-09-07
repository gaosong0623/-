#_author:无言宝宝
#date:  2019/8/1

#登录模块
import json
import os
import sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from mudule import The_main_interface
from mudule import Check_bank_card_statement
Amount=10000


def loading():
    import time
    for i in range(101):
        print('\r'+'>'*i,'%d%%'%i,end='')
        time.sleep(0.1)


def Deposit_function():
    if os.path.getsize("../conf/Account information.txt")!=0: #如果文件不为空就打开文件
        f = open("../conf/Account information.txt", "r") #把里面的信息取出来
        USinfo = json.loads(f.read())
        f.close()
        USinfo[USaccount] = {"0": name, "1": USpassword, "2": payment_code, "3": cash, "4": Amount}
        f = open("../conf/Account information.txt", "w")
        data = json.dumps(USinfo)
        f.write(data)  # 账户：0：名字，1：登录密码 2：支付密码 3：余额 4:额度
        f.close()
        print("You have successfully registered, is jumping to the login screen for you...")
        logged_in()
        The_main_interface.Feature_selection()
    elif os.path.getsize("../conf/Account information.txt")==0: #如果文件为空
        f = open("../conf/Account information.txt", "w")
        USinfo={USaccount:{0: name,1:USpassword ,2:payment_code, 3:cash,4: Amount,5:"normal"}}
        data = json.dumps(USinfo)
        f.write(data)  # 账户：0：名字，1：登录密码 2：支付密码 3：余额 4:额度
        f.close()
        print("You have successfully registered, is jumping to the login screen for you...")
        logged_in()
        The_main_interface.Feature_selection()


def deposit():  # 存钱函数
    global cash
    cash = input("How much would you like to deposit?")  # 存钱
    print("Please put in your cash...")
    select = input("Please enter Y after the banknote is finished."
                   "If you want to cancel, please press Q.\n>>>").strip()  # 放入钞票后输入Y，取消输入Q
    if select == "Y":  # 放钞完毕
        print("Just a moment, please. We are checking your bill...")  # 正在检测钞票
        loading()
        logger = Check_bank_card_statement.get_logger()
        logger.critical("Deposit successfully!Your balance is %s $+%s $Amount" % (cash, Amount))
        print("\nDeposit successfully!Your balance is %s $+%s $Amount" % (cash, Amount)) # 存款成功，你的余额是
        Deposit_function()
    if select == "Q":
        print("If you do not deposit money into your account,"
              "the default credit card limit is 10000.When you need to deposit,"
              " you can open the deposit function to operate.")  # 不存钱的话信用卡默认额度10000
        cash = 0
        Deposit_function()
        The_main_interface.Feature_selection()
    else:
        print("请输入指定信息！")
        deposit()



def logged_in():
    global USaccount,USpassword
    USaccount = input("Please enter your account number：\n>>>") #输入账号
    USpassword = input("Please enter your login password：\n>>>") #密码
    f = open('../conf/Account information.txt')
    data=json.loads(f.read())
    if USaccount in data :
        if data[USaccount]["1"] == USpassword:
            f = open("../conf/logging status.txt", "w")
            logging_status = "logged in"
            f.write(logging_status)
            f.close()
            f = open("../conf/Current_login_account.txt", "w")
            f.write(USaccount)
            f.close()
            print("Login successful, jump to the previous screen for you...")#登录成功，正在为你返回之前的界面……
            The_main_interface.Feature_selection()
        elif data[USaccount]["1"] != USpassword:
            print("The account name or password is incorrect, please re-enter!")
            logged_in()

    elif USaccount not in data:
            print("The account name or password is incorrect, please re-enter!")
            logger()





def logger():  #判断是否登录
    f = open("../conf/logging status.txt", "r")
    logging_status=f.read()
    f.close()
    f = open("../conf/Current_login_account.txt", "r")
    Login_account= f.read()
    f.close()
    if logging_status=="Not logged in" and Login_account==None:
        f = open("../conf/Current login account.txt", "w")
        f.write("")
        f.close()
        logger()

    if logging_status=="Not logged in" :        #输入1进行登录，输入2进行注册
        User_login_and_registration_options=input("Enter 1 to enter the login interface.\nEnter 2 to register\n>>>").strip()
        if User_login_and_registration_options=="1":
            logged_in()

        if User_login_and_registration_options=="2":
            global name,USaccount,USpassword,payment_code
            name=input("Please enter your name：\n>>>") #姓名
            USaccount=input("Please enter your account number：\n>>>") #账号
            USpassword=input("Please enter your login password:\n>>>") #登录密码
            payment_code=input("Please enter your payment password:\n>>>") #支付密码
            if os.path.getsize("../conf/Account information.txt")>0:
                f = open("../conf/Account information.txt", "r")  # 把里面的信息取出来
                USinfo = json.loads(f.read())
                f.close()
                if USaccount not in USinfo.keys():
                    deposit()

                elif USaccount in USinfo.keys():
                    print("The account you want to register already exists. Please re-enter!")
                    logger()

        deposit()