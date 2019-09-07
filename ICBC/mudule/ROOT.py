#_author:无言宝宝
#date:  2019/8/15
import json
import os

def root():
    end1="""
    ============================
    
    1.查看所有账户名称
    2.修改用户登录密码
    3.修改用户支付密码
    4.紧急锁定账户
    5.解除账户锁定
    6.查看被锁定的账户
    7.备份账户信息
    按Q可退出本界面。
    ============================
    """

    print(end1)
    choose=input(">>>")
    if choose=="1":
        f = open('../conf/Account information.txt', "r")
        data = json.loads(f.read())
        f.close()
        for i in data:
            print(i)
        root()
    if choose=="2":
        print("请输入要修改密码的用户名：")
        USname=input(">>>").strip()
        print("请输入要为他更改的登录密码：")
        USpassword=input(">>>")
        f = open('../conf/Account information.txt', "r")
        data = json.loads(f.read())
        f.close()
        data[USname]["1"]=USpassword
        f = open('../conf/Account information.txt', "w")
        data=json.dumps(data)
        f.write(data)
        f.close()
        print("修改成功！")
        root()
    if choose == "3":
        print("请输入要修改密码的用户名：")
        USname = input(">>>").strip()
        print("请输入要为他更改的支付密码：")
        USpassword = input(">>>")
        f = open('../conf/Account information.txt', "r")
        data = json.loads(f.read())
        f.close()
        data[USname]["2"] = USpassword
        f = open('../conf/Account information.txt', "w")
        data = json.dumps(data)
        f.write(data)
        f.close()
        print("修改成功！")
        root()
    if choose == "4":
        print("请注意此操作会让该用户无法登录，\n无法操作任何功能，直到解除锁定，确认请输入Y，取消输入Q。")
        choose=input(">>>").strip()
        if choose=="Y":
            print("请输入要锁定的用户名：")
            USID=input(">>>").strip()
            f = open('../conf/Account information.txt', "r") #打开所有账户信息
            data = json.loads(f.read())   #取出所有
            f.close()
            data[USID]["5"]="unusual"   #把登录状态修改为不正常
            f = open('../conf/Account information.txt', "w")  # 打开所有账户信息
            data=json.dumps(data)
            f.write(data)   #把修改后的信息存进去
            f.close()
            f = open("../conf/Lock_account.txt", "a")
            f.write(USID)
            f.close()

            print("锁定%s账户成功！"%(USID))
            root()

        if choose=="Q":
            print("已取消操作。")
            root()
        elif True:
            print("请输入标准选项！")
            root()

    if choose == "5": #解锁账户
        if os.path.getsize("../conf/Lock_account.txt")!=0:
            print("请输入要解锁的用户名：")
            USID = input(">>>").strip()
            f = open('../conf/Account information.txt', "r")  # 打开所有账户信息
            data = json.loads(f.read())  # 取出所有
            f.close()
            data[USID]["5"] = "normal"  # 把登录状态修改为正常
            f = open('../conf/Account information.txt', "w")  # 打开所有账户信息
            data = json.dumps(data)
            f.write(data)  # 把修改后的信息存进去
            f.close()
            f = open("../conf/Lock_account.txt", "r")
            info=f.read()
            f.close()
            info=info.replace(USID,"")
            f = open("../conf/Lock_account.txt", "w")
            f.write(info)
            f.close()
            print("解锁成功！")
            root()
        elif True:
            print("没有被锁定的账号，无法操作解锁！")
            root()

    if choose == "6":
        if os.path.getsize("../conf/Lock_account.txt") != 0:
            f = open("../conf/Lock_account.txt", "r")
            info = f.read()
            f.close()
            print("以下是全部被锁定的账号信息：\n%s"%(info))
            root()
        elif True:
            print("没有被锁定的账号，无法查看被锁定的账号！")
            root()

    if choose == "7":
        f = open('../conf/Account information.txt', "r")  # 打开所有账户信息
        data = json.loads(f.read())  # 取出所有
        f.close()
        data=json.dumps(data)
        f = open('../conf/Backup.txt', "w")  # 打开所有账户信息
        f.write(data)  # 取出所有
        f.close()
        print("备份成功！")
        root()

    if choose =="Q":
        exit("感谢使用！")

    elif True:
        print("请输入标准选项！")
        root()

root()