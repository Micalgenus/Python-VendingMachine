#-*- coding: utf-8 -*-

# 숫자인지 판단
def isNumber(s):
  try:
    float(s)
    return True
  except ValueError:
    return False
