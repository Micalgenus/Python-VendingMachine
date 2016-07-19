#-*- coding: utf-8 -*-

from mprint import *

# 동전 클래스
class Coin:
  value = 0

  def __init__(self, v):
    self.value = v

  def getCoin(self):
    return self.value

# 돈을 관리하는 클래스
class Money:
  # 돈의 종류 및 갯수
  money = { }
  # 화폐 단위
  unit = ""
  # 사용자가 넣은 동전
  user = [ ]
  # 잔액
  change = 0

  # 돈의 종류 설정
  def setMoney(self, value):
    self.money = value
  # 화폐 단위 설정
  def setUnit(self, value):
    self.unit = value
  # 동전 갯수 설정
  def setCoin(self, coin, value):
    self.money[coin] = value
  # 잔액 반환
  def getChange(self):
    return self.change
  # 화폐 단위 반환
  def getUnit(self):
    return self.unit
  # 동전 종류 수 반환
  def getCoinsNum(self):
    return len(self.money)
  # 동전 종류 전체 반환
  def getCoins(self):
    return self.money

  # 초기화
  def __init__(self):
    self.setUnit("")
    self.setMoney({ })

  # 동전 출력
  def printMoney(self):
    # 가지고 있는 돈
    for i in self.money:
      print i + self.unit + " : " + str(self.money[i]) + "개"
    # 들어온 돈
    printf("들어온 돈 : [ ")
    for p in self.user:
      printf(p.getCoin() + self.unit + ", ")
    print (" ]")
    # 잔액
    print ("잔돈 : " + str(self.change))
  # 돈 넣음
  def inputMoney(self, value):
    for i in self.money:
      if (i == value):
        self.money[i] += 1
        self.user += [ Coin(value) ]
        self.change += int(value)
        return "OK"
    return "NO"
  # 존재하는 화폐인지 검색
  def searchCoin(self, coin):
    for i in self.money:
      if (i == coin):
        return True
    return False
  # 돈 사용
  def useChange(self, money):
    self.change -= money
  # 동전이 있는지 검사
  def isEmpty(self):
    for i in self.money:
      if (self.money[i] != 0):
        return False
    return True

  # 잔돈 상황 파악
  # 5개 이하가 될 경우 잔돈이 없음으로 판단
  def exchangeable(self):
    for i in self.money:
      if (self.money[i] <= 5):
        return False
    return True
  # 잔돈 제거
  def changeRemove(self):
    self.change = 0
    for n in range(0, len(self.user)):
      for i in self.user:
        self.user.remove(i)
        break;
  # 돈 꺼냄
  # 잔액 반환시 사용자에게 주는 돈
  def removeCoin(self, n):
    for i in self.money:
      if (i == n):
        self.money[i] -= 1
        break
  # 돈을 금액별로 정렬 후 반환
  def sorted_coin(self):
    keylist = self.money.keys()

    new_key = { }

    for i in keylist:
      new_key[int(i)] = self.money[i]

    new = new_key.keys()
    new.sort()

    result_key = [ ]
    
    for key in new:
      result_key.append(key)

    return result_key

# 돈 입추가
def money_input(money):
  printf("넣으실 동전을 입력해 주십시오. : ")
  while True:
    m = raw_input()

    if (money.inputMoney(m) == "OK"):
      return money
    else:
      printf("동전을 하나씩 넣어주세요. ")

# 잔액 반환
def return_coins(coins):
  change = coins.getChange()
  skey = coins.sorted_coin()
  skey.reverse()

  V = { }
  # 가장 큰 돈부터 반환해줌
  for i in skey:
    V[i] = 0
    while i <= change:
      change -= i
      coins.removeCoin(str(i))
      V[i] += 1

  # 잔액 반환 하였으므로 제거
  coins.changeRemove()

  # (자판기 동전, 반환된 동전) 반환
  return (coins, V)
