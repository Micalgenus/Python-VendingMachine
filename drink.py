#-*- coding: utf-8 -*-

import random

from mprint import *

# 랜덤 가격
random_price = 800

# 음료 클래스
class Can:
    name = ""

    def __init__(self, n):
        self.name = n

    def getName(self):
        return self.name

# 음료 전체를 관리하는 클래스
class Drink:
  # 음료 종류
  can = { }
  # 현재 자판기에 있는 음료
  cans = [ ]

  # 음료 종류 설정
  def setCan(self, value):
    self.can = value
  #음료 가격 설정
  def setPrice(self, c, v):
    self.can[c] = v
  # 음료 종류 반환
  def getDrink(self):
      return self.can
  # 음료 종류 갯수 반환
  def getCount(self):
    n = 0
    for i in self.can:
        n += 1
    return n
  # 음료 이름을 기준으로 현재 자판기에 있는 갯수 반환
  def getCountName(self, name):
    n = 0
    for i in self.cans:
        if (i.getName() == name):
            n += 1
            
    return n
  # 음료 이름을 기준으로 가격 반환
  def getPriceName(self, name):
    for i in self.can:
      if (i == name):
        return self.can[i]
  # 음료 가격을 리스트화(전체)하여 반환
  def getPriceAll(self):
    p = [ ]
    for i in self.can:
        p.append(self.can[i])

    for i in range(0, 5 - self.getCount()):
        p.append(0)

    # 랜덤 가격
    p.append(random_price)
        
    return p
  # 음료 이름을 리스트화(전체)하여 반환
  def getCanAll(self):
    n = [ ]
    for i in self.can:
        n.append(i)
    #음료가 없는 경우
    for i in range(0, 5 - self.getCount()):
        n.append("None")

    # 랜덤
    n.append("Random")
        
    return n
  # 자판기에 있는 음료를 리스트화(전체)하여 반환
  def getCountAll(self):
    n = [ ]
    for i in self.can:
        n.append(self.getCountName(i))

    for i in range(0, 5 - self.getCount()):
        n.append(0)

    return n
  # 객체 초기화
  def __init__(self):
    self.setCan({ })
  # 현재 들어있는 음료의 가격과 갯수를 출력
  def printCan(self):
    for i in self.can:
      print i + " : " + str(self.can[i]) + ", " + str(self.getCountName(i)) + "개"
  # 음료를 넣는다
  def insertCan(self, can):
      for i in self.can:
          if (i == can):
              # 객체 생성
              self.cans.append(Can(can))
              return "OK"
            
      return "NO"
  # 음료를 꺼낸다
  def removeCan(self, can):
      for i in self.cans:
          if (i.getName() == can):
              # 객체 삭제
              self.cans.remove(i)
              break
  # 존재하는 음료인지 판단
  def checkName(self, name):
      for i in self.can:
          if (i == name):
              return True
      return False
  # 음료 종류를 추가
  def addDrink(self, can, price):
      self.can[can] = price

  def delDrink(self, can):
      del self.can[can]

# 음료를 선택
def select_can(drinks, coins):
  printf("음료를 선택해 주십시오. : ")
  while True:
    c = raw_input()
    # n = 잔액
    n = coins.getChange()
    if (drinks.checkName(c) == True):
        # p = 가격
        p = drinks.getPriceName(c)
        # 구매 가능한지 체크
        if (p > n):
            return (drinks, coins, "돈이 부족해용")
        # 음료가 남아있는지 체크
        elif (drinks.getCountName(c) == 0):
            return (drinks, coins, "매진된 음료에용")
        # 실제 구매
        else:
            coins.useChange(p)
            drinks.removeCan(c)
            return (drinks, coins, c + "가 나왔어용")
    # 랜덤을 선택
    elif (c == "Random" or c == "random"):
        # 돈이 되는지 판단
        if (random_price > n):
            return (drinks, coins, "돈이 부족해용")
        n = drinks.getCanAll()
        # 남은 음료중 선택
        while True:
            k = random.randrange(0, drinks.getCount())
            if (drinks.getCountName(n[k]) != 0):
                break

        # 구매
        coins.useChange(random_price)
        drinks.removeCan(n[k])
        return (drinks, coins, n[k] + "가 나왔어용")
        
    else:
        printf("음료 이름을 제대로 입력해 주세요. ")
