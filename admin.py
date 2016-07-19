#-*- coding: utf-8 -*-

from menu import *
from drink import *
from function import *

# 동전 관리
def change_coin(coins):
    # 동전 상황 출력
    coins.printMoney()
    printf("변경하실 동전을 고르세요. ")
    while True:
        c = raw_input()
        # 동전 검색
        if (coins.searchCoin(c)): break
        else:
            printf("올바른 동전을 선택해 주십시오. ")

    printf("변경하실 갯수를 입력하세요. ")
    while True:
        # 변경할 수 입력
        v = raw_input()
        if (isNumber(v)): break
        else:
            printf("변경하실 갯수를 입력해 주십시오. ")

    # 동전 갯수 변경
    coins.setCoin(c, int(v))
    return coins

# 화폐 관리
def change_munit(coins):
    # 화폐 변경시 남아있는 돈이 사라지게 됩니다.
    if (coins.isEmpty() == False):
        print "변경시 남은 동전이 사라지게 됩니다."
        while True:
            printf("계속 진행하시겠습니까? (Y / N) ")
            yn = raw_input()
            if (yn == "Y" or yn == "y"):
                break
            elif (yn == "N" or yn == "n"):
                return coins

    # 변경될 화폐 단위
    printf("변경할 화폐 단위를 입력하세요. ")
    # 한글로 입력될 경우
    c = raw_input().decode('euc-kr').encode('utf-8')
    # 한글 인코딩
    coins.setUnit(c)
    v = { }
    while True:
        printf("동전 가치를 입력하세요. (0 입력시 종료) : ")
        c = raw_input()
        if (isNumber(c)):
            if (c == "0"): break
            v[c] = 0
        else:
            print "올바른 동전을 입력해 주십시오. "

    # 동전 변경
    coins.setMoney(v)
    # 기존에 있는 잔돈 삭제
    coins.changeRemove()
        
    return coins

# 음료 갯수 추가, 제거
def change_can(drinks):
    printf("변경하실 음료를 선택해 주십시오. : ")
    while True:
        # 음료 입력
        c = raw_input()
        if (drinks.checkName(c)): break
        else:
            printf("음료 이름을 제대로 입력해 주세요. ")

    # 객체 단위이므로 1개씩 증감한다
    while True:
        printf("1개 추가 A, 1개 제거 S : ")
        v = raw_input()
        if (v == "A" or v == "a"):
            # 음료 증가
            drinks.insertCan(c)
            break
        elif (v == "S" or v == "s"):
            # 음료 감소
            drinks.removeCan(c)
            break

    return drinks

# 음료 종류 추가
def add_drink(drinks):
    # 음료가 출력 가능한 최대치인지 판단
    if (drinks.getCount() == 5):
        print "음료 갯수 최대치 입니다."
        return drinks
    else:
        # 음료 이름 입력
        printf("추가하실 이름을 입력해 주세요. ")
        while True:
            # 음료 중복 체크
            n = raw_input()
            if (drinks.checkName(n)):
                printf("이미 들어가 있는 음료입니다. ")
            else:
                break
                

        # 음료 가격 설정
        while True:
            printf("가격을 입력해 주십시오. ")
            p = raw_input()
            if (isNumber(p)): break

        # 음료 추가
        drinks.addDrink(n, int(p))

        return drinks

# 음료 종류 삭제
def del_drink(drinks):
    # 음료가 없을 경우 할 수 없음
    if (drinks.getCount() == 0):
        print "음료가 없습니다."
        return drinks
    else:
        # 음료 이름 검색
        printf("삭제하실 이름을 입력해 주세요. ")
        while True:
            c = raw_input()
            if (drinks.checkName(c)): break
            else:
                printf("음료 이름을 제대로 입력해 주세요. ")

        # 기존에 있는 음료 모두 제거
        n = drinks.getCountName(c)
        for i in range(0, n):
            drinks.removeCan(c)

        # 음료 리스트에서 제거
        drinks.delDrink(c)

        return drinks

# 음료 가격 설정
def change_price(drinks):
    # 음료가 없을 경우 할 수 없음
    if (drinks.getCount() == 0):
        print "음료가 없습니다."
        return drinks
    else:
        # 음료 이름 입력
        printf("변경할 음료의 이름을 입력해 주세요. ")
        while True:
            c = raw_input()
            if (drinks.checkName(c)): break
            else:
                printf("음료 이름을 제대로 입력해 주세요. ")

        # 설정할 가격 입력
        while True:
            printf("가격을 입력해 주십시오. ")
            p = raw_input()
            if (isNumber(p)): break

        # 음료 가격 설정
        drinks.setPrice(c, int(p))

        return drinks
    
def admin_mode(coins, drinks):
    print "관리자 모드로 진입하셧습니다."
    while True:
        c = select_admin()
        if (c == "money"): # 동전 관리
            coins = change_coin(coins)
        elif (c == "munit"): # 화폐 단위 관리
            coins = change_munit(coins)
        elif (c == "dnum"): # 음료 증가, 감소
            drinks = change_can(drinks)
        elif (c == "dadd"): # 음료 추가
            drinks = add_drink(drinks)
        elif (c == "ddel"): # 음료 삭제
            drinks = del_drink(drinks)
        elif (c == "dprice"): # 음료 가격 설정
            drinks = change_price(drinks)
           
        elif (c == "exit"):
            return coins
        else:
            printf("올바른 메뉴를 선택해 주십시오. ")

