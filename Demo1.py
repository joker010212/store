#   1      实现输入10个数字，并打印10个数的求和结果
'''
i=0
sum=0
while i <= 9:
    a = int(input("请输入想要求和的数"))
    i+=1
    sum=sum+a
    print("您输入的累加和为：", sum)

'''
#      2     从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
'''
i=0
sum=0
b=0
while i <= 9:
    a = int(input("请输入想要求和的数"))
    i+=1
    sum=sum+a
    if i<=9:
        pass
    else:
        print("您的累加和为：",sum)
        print("您的平均数为：",sum/10)
    if a >= b:
        b = a
        print("您的输入的最大数为", b,"\n")
    else:
        b=b
        print("您的输入的最大数为", b,"\n")
'''
#    3   使用random模块，如何产生 50~150之间的数？
'''
import random
data = random.randint(50, 150)
print("随机数来了：",data)
'''

#     4       从键盘输入任意三边，判断是否能形成三角形，
# 若可以，则判断形成什么三角形
# （结果判断：等腰，等边，直角，普通，不能形成三角形。）
'''
a=int(input("请输入第一条边"))
b=int(input("请输入第二条边"))
c=int(input("请输入第三条边"))
if (a+b>c&a-b<c)|(c+b>a&c-b<a)|(a+c>b&a-c<b):
    print("能生成三角形")
    if a == b == c:
        print("该三角形为等边三角新")
    elif (a == b != c) | (a == c != b )| (c == b != a):
        print("该三角形为等腰三角新")
    elif (a ** 2 + b ** 2 == c ** 2 )|( b ** 2 + c ** 2 == a ** 2 )| (a ** 2 + c ** 2 == b ** 2):
        print("该三角形为直角三角形")
    else:
        print("该三角形是一个普通三角形")
else:
    print("不能形成三角形")
'''
#      5        有以下两个数，使用+，-号实现两个数的调换。
'''
a=56
b=78
a,b=b,a
print("a=:",a,"b=:",b)
'''
#       6        实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
'''
name = 'root'  # 正确的用户名
passwd = 'admin'  # 正确的密码
o=[5,4,3,2,1,0]
for i in range(0, 3):
    usr_name = input("用户名：")
    usr_passwd = input("密码：")
    if usr_name == name and usr_passwd == passwd:
        print("欢迎使用蛇皮怪的电脑")
        break
    elif name != usr_name or passwd != usr_passwd:
        if i < 2:
            print("用户名密码错误，请重新输入！")
        else:
            print("电脑将在5秒后自毁")
            for p in o:
                print(p)
'''
#       7     编程实现下列图形的打印(三角形*号打印)
'''
for i in range(5):
    for j in range(0, 5- i):
        print(end=" ")
    for k in range(5 - i, 5):
        print("*", end=" ")
    print("")
'''
#        8      使用while循环实现99乘法表的打印。
'''
i=0
while i<9:
    i+=1
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i * j), end='' )
    print('\n')
'''
#        9        一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，
#        晚上下滑2米，问第几天能出来？请编程求出。
'''
h=20
up=3
down=2
for i in range(1,20):
    h=h-up
    if h<=0:
        print("第",i,"天爬出来了！！！！\n用了：", i, "天")
        break
    h=h+down
    if h>0:
        print("第",i,"天。没爬出来，爬了",20-h,"米")
'''
#         10          用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
nb=0
u=1
#当a=1时开始
while u<=20:
    a=u
    num = 1
    for i in range(1, a + 1):
        num *= i
    print("第",a,"阶乘为",num)
    u+=1
    nb = num + nb
print("1到20 阶乘的和为：",nb)
