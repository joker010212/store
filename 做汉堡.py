from threading import Thread
import time

quantity = 0
money = 100


class customer (Thread) :
    hamburg = 0
    yuanzhong = ''
    def run(self) -> None:
        global quantity,money
        while True :
            if  quantity > 0 and quantity <= 500:
                quantity -= 1
                self.hamburg += 1
                money -= 5
                print('恭喜',self.yuanzhong,'已经抢到一个汉堡,你已经抢到了',self.hamburg ,'个汉堡,还剩',money,'块钱!')
            elif money <= 0:
                print('穷鬼,没钱了快滚!')
                break


class cook (Thread) :
    chef = ''
    def run (self) -> None :
        global quantity,money
        while True :
            if quantity < 10 and money>0:
                time.sleep(1)
                quantity = quantity+1
                print(self.chef,'正在加班加点造汉堡,别催了!','现在汉堡库存还有',quantity,'个!')
            elif quantity >= 10 and money>0:
                time.sleep(1)
                print(self.chef,'已经造了',quantity,'个汉堡了,厨师们要累死了,歇3秒!')
            elif money<=0:
                print("跳出循环，还有："
                      "",money)
                break


y1 = customer()
y1.yuanzhong = '牛马'
y1.start()

y2 = customer()
y2.yuanzhong = '牛马2'
y2.start()

y3 = customer()
y3.yuanzhong = '牛马3'
y3.start()

y4 = customer()
y4.yuanzhong = '牛马4'
y4.start()

y5 = customer()
y5.yuanzhong = '牛马5'
y5.start()

y6 = customer()
y6.yuanzhong = '牛马6'
y6.start()

c1 = cook()
c1.chef = '王守义11香'
c1.start()

c2 = cook()
c2.chef = '王守义12香'
c2.start()

c3 = cook()
c3.chef = '王守义13香'
c3.start()
