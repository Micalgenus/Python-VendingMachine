#-*- coding: utf-8 -*-

from mprint import *

# 프로그램 메뉴 출력
def select_menu():
    print_menu()
    printf("메뉴를 선택해 주십시오. : ")
    while True:
        menu = raw_input()
        # 프로그램 종료
        if (menu == "0"): return "exit"
        # 돈 추가
        elif (menu == "1"): return "input"
        # 음료 선택
        elif (menu == "2"): return "choice"
        # 잔돈 반환
        elif (menu == "3"): return "return"
        # 관리자 모드
        elif (menu == "14004"): return "admin"
        # 잘못된 입력일 경우 재 입력
        else:
            printf("올바른 메뉴를 입력해 주십시오. ")

# 관리자 모드 메뉴            
def select_admin():
    print_admin()
    printf("메뉴를 선택해 주십시오. : ")
    while True:
        menu = raw_input()
        # 관리자 모드 종료
        if (menu == "0"): return "exit"
        # 동전 관리
        elif (menu == "1"): return "money"
        # 돈 단위 관리
        elif (menu == "2"): return "munit"
        # 음료 갯수 관리
        elif (menu == "3"): return "dnum"
        # 음료 종류 증가
        elif (menu == "4"): return "dadd"
        # 음료 종류 삭제
        elif (menu == "5"): return "ddel"
        # 음료 가격 변경
        elif (menu == "6"): return "dprice"
        
        else:
            printf("올바른 메뉴를 입력해 주십시오. ")
