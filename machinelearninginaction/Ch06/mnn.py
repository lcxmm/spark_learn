# -*-coding:utf-8-*-

from numpy import *
from copy import copy
import time, random

# 初始状态， 订单生产顺序， 随机生成， n:订单的个数。
def order(n):
    a = range(1, n + 1)
    random.shuffle(a)
    return a
# 初始接受顺序， 随机产生 0/1
def accept(n):
    acceptlist = []
    for i in range(n):
        acceptlist.append(random.randrange(0, 2, 1))
    return acceptlist
# 收益列表， 随机产生，500-1000 小数
def gain(n):
    gainlist = []
    for i in range(n):
        gainlist.append(random.uniform(500, 1000))
    return gainlist
# 生产时间列表， 随机产生 1-100 小数
def orderTime(n):
    timelist = []
    for i in range(n):
        timelist.append(random.uniform(1, 100))
    return timelist

# 订单需要的时间， a:订单需要时间的列表   m:机器的个数
# 返回的为交货时间表。 e.s [4, 6, 3, 0, 8, 7, 14, 9, 15, 14]
def times(y, m):
    delivery  = [] # 交货列表
    t = []
    for i in range(m):
        t.append(0)

    for i in range(y.shape[1]):
        delivery.append(0)
        index = t.index(min(t))
        # 如果第二行接受向量为 0 ， 直接交货，则交货时间为 0
        if y[1, i] == 0:
            delivery[i] = 0
            continue
        t[index] = t[index] + y[3, i]
        delivery[i] = t[index]
    return delivery

# 矩阵 matrix(mat) LN1
def LN1(y):
    column = y.shape[1]
    i = random.randrange(0, column , 1) # or random.randint(1, column + 1)
    while True:
        j = random.randrange(0, column, 1)
        if j != i:
            break
        time.sleep(1)
        print "     LN1产生的两个随机数相同，休息1s，重新生成"
    tmp = array(y[0:, i])
    y[0:, i] = y[0:, j]
    y[0:, j] = mat(tmp)
    return y
# 改变 0 or 1   LN2
def LN2(y):
    column = y.shape[1]
    i = random.randrange(0, column, 1)
    flag = y[1, i]
    if flag :
        y[1, i] = 0
    else:
        y[1, i] = 1
    return y
# k是振动次数
def SN(y, k):
    for i in range(k):
        y = LN1(copy(y))
        y = LN2(copy(y))
    return y

def sumGain(y , deadline, r): # r 惩罚系数
    delivery = times(y, y.shape[1])
    money = 0
    for i in range(len(delivery)):
        tmp = y[2, i] - r* max(0, delivery[i] - deadline)
        money = money + y[1, i]*tmp
    return money

def main(n, m):
    r = 10
    y = [] # 初始方案

    deadline = random.uniform(1, m*n*45 + 1)
    # y 为 4*n 矩阵， 第一行为订单生产顺序，  第二行为接受顺序， 第三行为 订单收益， 第四行为订单完成时间
    y.append(order(n))
    y.append(accept(n))
    y.append(gain(n))
    y.append(orderTime(n))
    y = mat(y)

    k = 1

    iteration = 20

    for i in range(iteration):
        print "     local search: iteration times = {0}".format(i)
        if k >= 3:
            k = 1
        ysum = sumGain(y, deadline, r)
        targetsum = ysum
        y1 = SN(copy(y), k)
        y1sum = sumGain(copy(y1), deadline, r)

        flag = random.randrange(0, 2, 1)
        if flag :
            y2 = LN1(y1)
        else:
            y2 = LN2(y1)
        y2sum = sumGain(copy(y2), deadline, r)

        planlist = [y, y1, y2]
        sumlist = [ysum, y1sum, y2sum]
        if targetsum == max(sumlist):
            k = k + 1
        else:
            k = 1
            targetsum = max(sumlist)
            index = sumlist.index(targetsum)
            y = copy(planlist[index])
        print "         this iteration get k = {0}".format(k)
        print "         this iteration get targetsum = {0}".format(targetsum)
    print "final return targetsum = {0}".format(targetsum)
    return targetsum

if __name__ == "__main__":
    n = 10 # 订单数
    m = 3  # 机器数
    repeatimes = 20
    repeatsum = []
    start = time.clock()
    for i in range(repeatimes):
        print "repeat {0} times".format(i)
        repeatsum.append(main(n, m))
    end = time.clock()
    print "For {0} times, max value  = {1}".format(repeatimes, max(repeatsum))
    print "For {0} times, min value  = {1}".format(repeatimes, min(repeatsum))
    print "For {0} times, avg value  = {1}".format(repeatimes, sum(repeatsum)/repeatimes)
    print "For {0} times, need times = {1}".format(repeatimes, end - start)