#_author:无言宝宝
#date:  2019/8/1
import json
from mudule import The_main_interface
from mudule import Check_bank_card_statement

def loading():
    import time
    for i in range(101):
        print('\r'+'>'*i,'%d%%'%i,end='')
        time.sleep(0.1)

#转账功能  1.输入账号和支付密码，核对 2.输入要转多少钱，
def transfer():
    print("Welcome to use the ICBC transfer function.")
    select=input("To transfer the input Y,\nreturn to the main menu and enter Q!\n>>>").strip()
    if select=="Y":
        USaccount = input("Please enter your account number：\n>>>") #账号
        payment_code = input("Please enter your payment password:\n>>>")  # 支付密码
        f = open('../conf/Current_login_account.txt')
        data=f.read()
        f.close()
        if USaccount==data:#判断登录账号和输入的账号是否一致
            f = open("../conf/Account information.txt", "r")  # 把里面的信息取出来
            USinfo = json.loads(f.read())
            f.close()
            if USinfo[USaccount]["2"]==payment_code:#判断账号和支付密码是否对应
                global Account_to_transfer
                Account_to_transfer=input("Please enter the account you want to transfer:").strip() #要转钱的账号
                difference=int(input("Please enter the money you want to transfer to the other party:").strip()) #要转多少钱
                Account_Balance=int(USinfo[USaccount]["3"])
                if Account_Balance>=difference: #判断账户上钱够不够 (账户余额大于等于你要转的钱）
                    print("Account:%s,\nDo you want to transfer money to:%s,\n%s RMB?\n"%(USaccount,Account_to_transfer,difference))
                    select=input("If you confirm, please enter Y, cancel please enter Q\n>>>").strip()
                    if select=="Y":#如果确定：判断账号是否存在！如果存在，就扣钱！给对方加钱！
                        if Account_to_transfer in USinfo.keys():#如果对方的账号存在：
                            Account_Balance=Account_Balance-difference #你账户的余额减去你要转的钱=你现在的余额
                            OTHAccount_Balance=int(USinfo[Account_to_transfer]["3"]) #要转账账号的余额
                            OTHAccount_Balance=OTHAccount_Balance+difference #你朋友的账户余额=她原本的余额+你转给她的钱
                            USinfo[USaccount]["3"]=Account_Balance #修改你账号的余额
                            USinfo[Account_to_transfer]["3"]=OTHAccount_Balance #修改你朋友账号的余额
                            f = open("../conf/Account information.txt", "w")  # 把里面的信息取出来
                            USinfo=json.dumps(USinfo)
                            f.write(USinfo)
                            f.close()
                            loading()
                            logger = Check_bank_card_statement.get_logger()
                            logger.critical("The transfer to:%s was successful.Operating transfer amount:%s,Your current balance is:%s Yuan."%(Account_to_transfer,difference,Account_Balance))
                            print("\nThe transfer was successful.money will arrive soon!")
                            transfer()
                        elif Account_to_transfer not in USinfo.keys():
                            print("The account you want to transfer does not exist,\n please check it before proceeding!")
                            transfer()

                    if select=="Q":#取消转账
                        print("I have cancelled the transfer operation for you and returned to the main menu,\n thank you for your use!")
                        transfer()
                if Account_Balance<difference:# 账户余额小于你要转的钱
                    print("Insufficient balance, please re-operate!")
                    transfer()

            elif USinfo[USaccount]["2"]!=payment_code:#支付密码错误
                print("The payment password is incorrect, please re-enter!\nPlease note: you need to enter the payment password instead of the login password!")
                transfer()
        elif USaccount!=data:
            print("The account you entered does not match the account you are logged in to, please re-enter!")
            transfer()

    if select=="Q":
        print("Jumping interface for you, please wait...")
        The_main_interface.Feature_selection()

    elif select!="Q" and select!="Y":
        print("Please enter the standard options!")
        transfer()