#!/usr/bin/python3
'''
This program is to generate the most positive delta as to figure out when to trade
Each element in the array corresponds to times during the day
'''
import time

#Figure out the biggest delta in 1D array
def bestTime(prices):
    buy, sell = 0,0
    for indexbuy, i in enumerate(prices):
        j = i + 1
        for indexsell, j in enumerate(prices):
            result = j - i
            if result > (sell-buy):
                buy,sell = i,j
    return buy, sell
#Figure out biggest delta in 2D array
def bestTime2D(prices):
    buy = [0,0,0,0]
    sell = [0,0,0,0]
    for indexbuy, index in enumerate(prices):
        for indexbuy2, i in enumerate(index):
            #print(indexbuy2)
            for indexsell, jindex in enumerate(prices):
                
                for indexsell2, j in enumerate(jindex):
                    
                    if i !='\n' and j !='\n':
                        
                        result = float(j) - float(i)
                        if result > (sell[indexsell2]-buy[indexbuy2]):
                            buy[indexbuy2],sell[indexsell2] = float(i),float(j)
    #print(buy)
    #print(sell)
    return buy, sell


#start_time = time.time()
#buy,sell = bestTime(prices)
#end_time = time.time()

#print("You should buy at €{0} and sell at €{1}".format(buy,sell))
#print("Execution time is {0} milliseconds".format((end_time-start_time)*1000))

#Creating the array of numbers

import random
f = open('tradefiles.txt', 'w')
i = 0
while i < 1000:
    if i ==0:
        a = round(random.uniform(200,600),2)
    else:
        flip_a_coin = random.uniform(0,10)
        if flip_a_coin > 5:
            a = round(a+random.uniform(0,10),2)
        else:
            a = round(a-random.uniform(0,10),2)
    if i != 0:
        f.write('{0},'.format(a))
        if i%4 ==0:
            f.write('\n')
    i+=1
f.close()

prices = []

f = open('tradefiles.txt', 'r')
for line in f.readlines():
    line = line[0:-2]
    line = line.strip()
    #print(line)
    prices.append(line.split(','))




#1st  attempt 38533.44821929932 milliseconds
#2nd attempt 31401.96990966797 milliseconds with for loops
#3rd  attempt 29932.20567703247 milliseconds enumerate


'''
Make a class, buyer, seller, broker

buyer has a balence
seller has to have stock available

broker has to ensure the buyer has enough money and check if the seller has stock
'''

class seller():

    def __init__(self, name):
        self.name = name
        self.current_stock_level = 2500

    def sell_stock(self,amount):
        if self.current_stock_level > amount:
            self.current_stock_level -= amount

    def return_stock(self,amount):
        self.current_stock_level += amount

class buyer():

    def __init__(self, balence,name):
        self.balence = balence
        self.name = name
        self.owned_stocks = {}

    def make_purchase(self,amount):
        if amount < self.balence:
            #print(self.balence)
            self.balence -= amount

    def sell_stock(self):
        self.balence+=amount

class broker():
    def __init__(self,client1,client2,amount,stock_price,buying):       
        self.client1 = client1 #buyer
        self.client2 = client2 #seller
        self.amount = amount
        self.price = stock_price
        self.buying = buying
        
    def conduct_exchange(self):
        cost = self.price*self.amount
        if self.buying == True:
            balence = self.client1.balence
            if balence > cost:
                if self.client2.current_stock_level > self.amount:
                    #print("333")
                    self.client1.make_purchase(cost)
                    self.client2.sell_stock(self.amount)
                    if self.client2.name in self.client1.owned_stocks.keys():
                        self.client1.owned_stocks[self.client2.name] += self.amount
                    else:
                        self.client1.owned_stocks[self.client2.name] = self.amount                       
        else:
            if self.client1.owned_stocks[self.client2.name] >= self.amount:
                self.client1.sell_stock()
                self.client2.return_stock(self.amount)
    

google = seller("GGL")
apple = seller("APP")
amazon = seller("AMA")
bloomberg = seller("BLB")

company = [google,apple,amazon,bloomberg]


fionn = buyer(4000,"Fionn")
richard = buyer(8000,"Richard")
brian = buyer(5000,"Brian")

buy = []
sell = []
start_time = time.time()
buy,sell = bestTime2D(prices)
#print(buy)
index = 0
mostprofit = 0
mostProfitableStock = 0
while index < len(buy):
    if (sell[index] - buy[index]) > mostprofit:
        mostProfitableStock = index
    index+=1

amount = round(fionn.balence/buy[mostProfitableStock])
trade_it = broker(fionn,company[mostProfitableStock],amount,buy[mostProfitableStock], True)
trade_it.conduct_exchange()
amount = round(richard.balence/buy[mostProfitableStock])
trade_it = broker(richard,company[mostProfitableStock],amount,buy[mostProfitableStock], True)
trade_it.conduct_exchange()
amount = round(brian.balence/buy[mostProfitableStock])
trade_it = broker(brian,company[mostProfitableStock],amount,buy[mostProfitableStock], True)
trade_it.conduct_exchange()
amount = fionn.owned_stocks[company[mostProfitableStock].name]
trade_it = broker(fionn,company[mostProfitableStock],amount,sell[mostProfitableStock], False)
trade_it.conduct_exchange()
amount = richard.owned_stocks[company[mostProfitableStock].name]

trade_it = broker(richard,company[mostProfitableStock],amount,sell[mostProfitableStock], False)
trade_it.conduct_exchange()
amount = brian.owned_stocks[company[mostProfitableStock].name]
trade_it = broker(brian,company[mostProfitableStock],amount,sell[mostProfitableStock], False)
trade_it.conduct_exchange()

end_time = time.time()


print("{0} new balence is €{1}".format(fionn.name,fionn.balence))
print("{0} new balence is €{1}".format(richard.name,richard.balence))
print("{0} new balence is €{1}".format(brian.name,brian.balence))
print("Execution time is {0} milliseconds".format((end_time-start_time)*1000))


