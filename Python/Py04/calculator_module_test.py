# [QUEST 04] 파이썬을 사용하여 간단한 계산기 프로그램 만들기

# 사용자로부터 두 개의 정수와 연산자(+,-,*,/,**)를 입력받아 계산 결과를 출력하는 프로그램을 만들어주세요

# 조건
# 사용자가 입력한 값이 정수가 아닌 경우 ValueError를 처리하여 적절한 오류 메시지를 출력해야 합니다
# 정수가 입력될 때 까지 잘못된 입력입니다. 정수를 입력해주세요."를 출력하며 다시 입력받기를 시도합니다.
# 나눗셈 연산 시 두 번째 정수가 0인 경우 ZeroDivisionError를 처리하여 적절한 오류 메시지를 출력합니다.
# 사용자가 지원하지 않는 연산자를 입력한 경우 적절한 오류 메시지를 출력합니다.
# math 모듈을 사용하여 제곱 연산(**)을 지원합니다.
# 계산기를 통해 계속 계산을 할 것인지 입력받습니다.

import math

def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("잘못된 입력입니다. 정수를 입력해주세요.")

def get_operator():
    while True:
        operator = input("연산자를 입력하세요 (+, -, *, /, **): ")
        if operator in ('+', '-', '*', '/', '**'):
            return operator
        else:
            print("지원하지 않는 연산자입니다. 다시 입력해주세요.")

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("0으로 나눌 수 없습니다.")
        return num1 / num2
    elif operator == '**':
        return math.pow(num1, num2)

def main():
    while True:
        print("\n계산기 프로그램")

        num1 = get_integer("첫 번째 정수를 입력하세요: ")
        num2 = get_integer("두 번째 정수를 입력하세요: ")
        operator = get_operator()

        try:
            result = calculate(num1, num2, operator)
            print(f"결과: {result}")
        except ZeroDivisionError as e:
            print(e)
        except Exception as e:
            print("예상치 못한 오류가 발생했습니다.", e)

        while True:
            again = input("계산을 계속하시겠습니까? (y/n): ").strip().lower()

            if again == 'y':
              break
            elif again == 'n':
              print("계산기를 종료합니다.")
              return
            else:
              print("잘못된 입력입니다. y또는 n을 입력해주세요.")

if __name__ == "__main__":
    main()