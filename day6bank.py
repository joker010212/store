'''
    中国工商银行账户管理系统：
        ICBC:
'''
import random
import time
# 1.准备一个数据库 和 银行名称
bank = {}  # 空的数据库
'''
    {
        "张三":{
            account:s001,
            country:"中国"
        }，
        "李四":{
        }
    }
'''
bank_name = "中国工商银行昌平回龙观支行"  # 银行名称写死的

# 2.入口程序
def welcome():
    print("*************************************")
    print("*         中国工商银行昌平支行         *")
    print("*************************************")
    print("*    1.开户                          *")
    print("*    2.存钱                          *")
    print("*    3.取钱                          *")
    print("*    4.转账                          *")
    print("*    5.查询                          *")
    print("*    6.Bye！                         *")
    print("**************************************")

# 银行的开户逻辑
def bank_addUser(account, username, password, country, province, street, gate, money):
    # 1.判断数据库是狗已满
    if len(bank) >= 100:
        return 3
    # 2.判断用户是否存在
    if account in bank:
        return 2
    # 3.正常开户
    bank[account] = {
        "account": account,
        "password": password,
        "country": country,
        "username": username,
        "province": province,
        "street": street,
        "gate": gate,
        "money": money,
        "bank_name": bank_name
    }
    return 1

def CQ():
    cqzz = int(input("请输入你要存钱的账号"))
    if cqzz in bank.keys():
        C = int(input("请输入你要存的钱数"))
        print("请放入您的钞票")
        print("...")
        bank[account]["money"] = bank[account]["money"]+C
        print("存钱成功")
    else:
        print("存钱失败")
def QQ():
    qqh = input("请输入你要取钱的账号")
    if qqh in bank:
        qqmm = int(input("请输入你要取钱的密码"))
        if qqmm in bank[qqh].values():
            qqq = input("请输入你要取钱的金额")
            if qqq < bank[account]["money"]:
                bank[account]["money"] =bank[account]["money"]-qqq
                print("请稍等...")
                time.sleep(1.5)
                print("取钱成功")
            else:
                print("转账失败")
        else:
            print("您的密码输入错误")
    else:
        print("您输入的账户错误")
def ZZ():
    zzh=input("请输入你的账号")
    if zzh in bank:
        zzmm = int(input("请输入你当前账户的密码"))
        if zzmm in bank[zzh].values():
            zzh = input("请输入你要转账的账号")
            if zzh in bank:
                zzq=input("请输入你要转账的金额")
                if zzq<bank[account]["money"]:
                    bank[account]["money"]=bank[account]["money"]-zzq
                    print("请稍等...")
                    time.sleep(1.5)
                    print("转账成功")
                else:
                    print("转账失败")
            else:
                print("无此账号")
        else:
            print("您的密码输入错误")
    else:
        print("您输入的账户错误")

def CX():
    cxzz=int(input("请输入你要查询的账号"))
    if cxzz in bank.keys():
        cxmm = int(input("请输入你要查询的密码"))
        if cxmm in bank[cxzz].values():
            print("您当前余额为：",bank[account]["money"])
        else:
            print("您的密码输入错误")
    else:
        print("您的账号输入错误")

while True:
    # 打印欢迎程序
    welcome()
    chose = input("请输入您的业务：")
    if chose == "1":
        account = random.randint(10000000, 99999999)
        username = input("请输入您的用户名：")
        password = int(input("请输入您的开户密码："))
        country = input("请输入您的国籍：")
        province = input("请输入您的居住省份：")
        street = input("请输入您的街道：")
        gate = input("请输入您的门牌号：")
        money = 0  # 将输入金额转换成int类型
        # 随机产生8为数字

        status = bank_addUser(account, username, password, country, province, street, gate, money)

        if status == 3:
            print("对不起，用户库已满，请携带证件到其他银行办理！")
        elif status == 2:
            print("对不起，该用户已存在！请勿重复开户！")
        elif status == 1:
            print("开户成功！以下是您的个人开户信息：")
            info = '''
                    ----------个人信息------
                    用户名：%s
                    密码：%s
                    账号：%s
                    地址信息
                        国家：%s
                        省份：%s
                        街道：%s
                        门牌号: %s
                    余额：%s
                    开户行地址：%s
                    ------------------------
                '''
            print(info % (username, password, account, country, province, street, gate, money, bank_name))
        time.sleep(3)
    elif chose == "2":
        CQ()
        time.sleep(3)
    elif chose == "3":
        QQ()
        time.sleep(3)
    elif chose == "4":
        ZZ()
        time.sleep(3)
    elif chose == "5":
        CX()
        time.sleep(3)
    elif chose == "6":
        print("欢迎下次光临！")
        break
    else:
        print("输入错误！请重新输入！")
