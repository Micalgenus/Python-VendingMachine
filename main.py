#-*- coding: utf-8 -*-

from menu import *
from init import *
from admin import *

# 메인
def main():
  # 파일 읽기 및 초기화
  (coins, drinks) = init()
  msg = ""
  V = ""
  while True:
    # 정보 출
    print_vm(drinks ,coins, msg)
    print_return(V, coins.getUnit())
    # V = 환전시 사용됨
    V = ""
    # msg = 출력 내용
    msg = ""
    # 사용자 입
    c = select_menu()

    # 종료, 종료하지 않을 경우 정보가 저장되지 않음
    if (c == "exit"):
      break
    # 관리자 모드
    elif (c == "admin"):
      coins = admin_mode(coins, drinks)
    # 돈 넣음
    elif (c == "input"):
      coins = money_input(coins)
    # 음료수 선택
    elif (c == "choice"): 
      # 잔돈 체크
      if (coins.exchangeable() != True):
        msg = "잔돈이 없어용."
      # 잔액 체크
      elif (coins.getChange() != 0):
        (drinks, coins, msg) = select_can(drinks, coins)
      # 잔액 부족
      else:
        msg = "Please enter your coins."
    # 잔액 반환
    elif (c == "return"):
      msg = "잔돈 " + str(coins.getChange()) + coins.getUnit() + "반환."
      (coins, V) = return_coins(coins)
      

  # 프로그램 종료시 정보 저장
  save_file(coins, drinks)

main()
