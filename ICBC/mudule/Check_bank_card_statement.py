#_author:无言宝宝
#date:  2019/8/1

#日志模块
import logging
import os
import sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from mudule import The_main_interface

def get_logger():

    f = open("../conf/Current_login_account.txt", "r")  # 拿到当前登录的用户名字
    account_name = f.read()
    f.close()
    logger=logging.getLogger() #先拿到logging对象
    data = BASE_DIR+"/logger/"+account_name+".log"
    fh=logging.FileHandler(data)#文件保存地址
    formatter=logging.Formatter("%(asctime)s %(message)s","%Y%b%d-%H:%M:%S")
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger



#调用方法：
# logger = Check_bank_card_statement.get_logger()
# logger.critical(放你要输入的内容)

def bill():
    f = open("../conf/Current_login_account.txt", "r")  # 拿到当前登录的用户名字
    account_name = f.read()
    f.close()
    The_path= BASE_DIR+"/logger/"+account_name+".log"
    f=open(The_path, "r")
    data=f.read()
    f.close()
    end1="""
    ========================================================
    
    hello,
    Thank you for using the billing inquiry service,
    For bill inquiry, please enter "Y",
    To return to the main menu, please enter "Q"
    
    =========================================================
    """
    print(end1)
    USinput=input(">>>").strip()
    end2="""
=============================================================
Here is your transaction bill:

"""
    if USinput=="Y":
        print(end2)
        print(data)
        end3="""
=============================================================

Thank you for using the billing inquiry service,     
To return to the main menu, enter "T",
To exit, enter Q

=============================================================   
        """
        print(end3)
        choose=input(">>>").strip()
        if choose=="T":
            The_main_interface.Feature_selection()
        if choose=="Q":
            print("Thank you for using ICBC,\nWe will make better optimization for you and wish you a happy life!")
            exit()

    if USinput=="Q":
        The_main_interface.Feature_selection()

    elif USinput != "Y" and USinput != "Q":
        print("Your input is not compliant, please re-enter!")
        bill()

