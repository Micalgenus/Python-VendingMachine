#-*- coding: utf-8 -*-

import sys
import os

# 개행 없는 출력
def printf(str):
    sys.stdout.write(str)

# 메뉴 출력
def print_menu():
    print "1. 돈 추가"
    print "2. 음료수 선택"
    print "3. 잔돈 반환"
    print "0. 프로그램 종료"

# 자판기 출력
def print_vm(drinks, coins, msg):
    u = coins.getUnit() # 화폐 단위
    p = drinks.getPriceAll() # 가격
    n = drinks.getCanAll() # 이름
    m = drinks.getCountAll() # 갯수
    c = coins.exchangeable() # 잔액 상황
    if (c == True):
        cc = " "
    else:
        cc = "잔돈없음"
        
    print  "    ─────────────────────────────"
    print  "  /                                                         /│"
    print  " /                                                         / │"
    print  "┌──────────────────────┬─────┐ │"
    print  "│                                            │          │ │"
    print  "│              Vending Machine               │          │ │"
    print  "│                                            │          │ │"
    print  "│  ┌────┐  ┌────┐  ┌────┐  │          │ │"
    print  "│  │        │  │        │  │        │  │          │ │"
    print  "│  │%8s│  │%8s│  │%8s│  │          │ │" % (n[0], n[1], n[2])
    print  "│  │        │  │        │  │        │  │          │ │"
    print  "│  │ %4d%2s │  │ %4s%2s │  │ %4s%2s │  │          │ │" % (p[0], u, p[1], u, p[2], u)
    print  "│  │  %2d개  │  │  %2d개  │  │  %2d개  │  │          │ │" % (m[0], m[1], m[2])
    print  "│  │        │  │        │  │        │  │          │ │"
    print  "│  └────┘  └────┘  └────┘  │          │ │"
    print  "│                                            │          │ │"
    print  "│  ┌────┐  ┌────┐  ┌────┐  │   Money  │ │"
    print  "│  │        │  │        │  │        │  │ %6d%2s │ │" % (coins.getChange(), u)
    print  "│  │%8s│  │%8s│  │%8s│  │          │ │" % (n[3], n[4], n[5])
    print  "│  │        │  │        │  │        │  │          │ │"
    print  "│  │ %4d%2s │  │ %4s%2s │  │ %4s%2s │  │ %8s │ │" % (p[3], u, p[4], u, p[5], u, cc)
    print  "│  │  %2d개  │  │  %2d개  │  │        │  │          │ │" % (m[3], m[4])
    print  "│  │        │  │        │  │        │  │          │ │"
    print  "│  └────┘  └────┘  └────┘  │          │ │"
    print  "│                                            │          │ │"
    print  "│                                            │          │ │"
    print  "│                                            │          │ │"
    print  "│   ┌─────────────────┐   │          │ │"
    print  "│   │                                  │   │          │ │"
    print  "│   │%34s│   │          │ │" % msg
    print  "│   │                                  │   │          │ │"
    print  "│   └─────────────────┘   │          │ /"
    print  "│                                            │          │/"
    print  "└──────────────────────┴─────┘"

# 관리자 모드 출력
def print_admin():
    print "1. 동전 갯수 관리"
    print "2. 화폐 단위 변경"
    print "3. 음료 갯수 관리"
    print "4. 음료 종류 추가"
    print "5. 음료 종류 삭제"
    print "6. 음료 가격 관리"
    print "0. 관리자 모드 종료"

# 잔돈 반환 결과 출력
def print_return(V, unit):
    if (V == ""):
        print ""
    else:
        printf("[ ")
        for i in V:
            printf(str(i) + unit + " : " + str(V[i]) + ", ")
        print ("]")
