#-*- coding: utf-8 -*-

import os

from money import *
from drink import *

# 초기화
def init():
    # 초기화 파일이 존재하지 않을 경우 기본적인 초기화 진행
    M = Money()
    D = Drink()
    if (os.path.exists("initionalization.txt") == False):
        # 기본 값으로 설정
        M.setUnit("원")
        M.setMoney({ "10" : 10, "50" : 10, "100" : 10, "500" : 10 })

        D.setCan({ "COKE" : 1000, "SODA" : 700 })
        for n in D.getDrink():
            for i in range(0, 5):
                D.insertCan(n)

        return (M, D)
    # 초기화 파일이 존재할 경우 파일에서 초기화
    else:
        f = open("initionalization.txt", "r")
        s = f.readline()
        V = { } # 음료 가격
        K = { } # 음료 갯수
        # 음료 받아옴
        for i in range(0, int(s)):
            c = f.readline().split()
            V[c[0]] = int(c[2])
            K[c[0]] = int(c[1])

        # 음료 설정
        D.setCan(V)
        for i in K:
            for j in range(0, K[i]):
                D.insertCan(i)

        # 돈 받아옴
        s = f.readline().split()
        M.setUnit(s[1])
        V = { }
        for i in range(0, int(s[0])):
            c = f.readline().split()
            V[c[0]] = int(c[1])

        # 돈 설정
        M.setMoney(V)
            
        f.close()

        return (M, D)

# 파일 저장
def save_file(coins, drinks):
    f = open("initionalization.txt", "w")
    # 음료 종류 수
    s = drinks.getCount()
    f.write(str(s) + "\n")
    p = drinks.getPriceAll() # 가격 저장
    c = drinks.getCanAll()   # 이름 저장
    n = drinks.getCountAll() # 갯수 저장
    for i in range(0, s):
        #  이름 + 갯수 + 가격
        f.write(c[i] + "\t" + str(n[i]) + "\t" + str(p[i]) + "\n")

    # 동전 종류 수 + 단위
    f.write(str(coins.getCoinsNum()) + "\t" + coins.getUnit() + "\n")
    m = coins.getCoins()
    for i in m:
        # 동전 값 + 갯수
        f.write(i + "\t" + str(m[i]) + "\n")
    
    f.close()
