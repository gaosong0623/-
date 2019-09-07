#_author:无言宝宝
#date:  2019/8/1


#余额查询

from mudule import The_main_interface


def Input_selection():
    select = input("Thank you for using the Query Balance feature."
                   "Press T to return to the main menu, press Q to exit\n>>>").strip()
    if select == "T":
        The_main_interface.Feature_selection()

    if select == "Q":
        exit("Thank you for using ICBC,"
             "We will make better optimization for you and wish you a happy life!")
    elif select!="Q"and select!="T":
        print("Your input is not recognized, please re-enter!")
        Input_selection()


def balance_enquiry(): #余额查询
    import json
    f = open("../conf/Current_login_account.txt", "r")
    account_number = f.read()
    f.close()
    f = open('../conf/Account information.txt', "r")
    data = json.loads(f.read())
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
    Input_selection()

