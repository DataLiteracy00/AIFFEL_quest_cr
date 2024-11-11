import random
from datetime import datetime

def get_datetime():
  now = datetime.now()
  return now.strftime('%Y-%m-%d %H:%M:%S')

def make_random_number(digits):
  return str(random.randint(1,10 ** digits)).zfill(digits)

def make_random_account():
  three_number = make_random_number(3)
  two_number = make_random_number(2)
  six_number = make_random_number(6)
  return f"{three_number}-{two_number}-{six_number}"

class Account:
  account_count = 0 # Q2. 클래스 변수 선언

  def __init__(self, depositor, balance):  # Q1. 매직 메서드 구현
    self.bank_name = '아이펠 은행'  # Q1. 은행 이름 미리 초기화
    self.account_num = make_random_account() # Q1. 계좌번호 랜덤 생성
    self.depositor = depositor # Q1. 예금주랑 잔액 입력 받기
    self.balance = balance # Q1. 예금주랑 잔액 입력 받기
    self.deposit_count = 0
    self.deposit_history_list = []
    self.withdraw_history_list = []
    Account.account_count += 1 # Q2. 계좌수 클래스 레벨에서 카운트

  def get_account_num(self): # Q3. 계좌 개수 출력 함수 선언
    return Account.account_count

  def deposit(self, money): # Q4. 입금하기 위한 메서드
    if money <= 0:
      print(f"입금은 최소 1원 이상만 가능합니다. 잔액 : {format(self.balance,',')}원")
    else:
      self.deposit_count += 1 # Q7. 이자 지급을 위한 deposit_count 올리기

      if self.deposit_count >= 5: # Q7. 이자 계산
        money += money * 1.01

      self.balance += money

      self.record_deposit_history(money)
      
  
  def withdraw(self, money): # Q5. 출금하기 위한 메서드
    if money > self.balance:
      print(f"계좌 잔액 이상 출금할 수 없습니다. 잔액 : {format(self.balance,',')}원")
    else:
      self.balance -= money
    
    # Q10. 입금 내역 기록 메서드 호출해서 money가 입금될때마다 기록되도록
    self.record_withdraw_history(money)
    
  def display_info(self): #Q6. 계좌 정보 출력 메서드
    print(f"은행이름: {self.bank_name}, 예금주: {self.depositor} 계좌번호: {self.account_num}, 잔고: {format(self.balance,',')}원")

  # Q10. 입금 내역 기록
  def record_deposit_history(self, money):
    current_time = get_datetime()
    self.deposit_history_list.append({"입금 시간 ": current_time, "금액 ": f"{format(money, ',')}원"})

  # Q10. 출금 내역 기록
  def record_withdraw_history(self, money):
    current_time = get_datetime()
    self.withdraw_history_list.append({"출금 시간 ": current_time, "금액 ": f"{format(money, ',')}원"})

  # Q10. 입금 내역 정보 출력
  def deposit_history(self):
    max_width = 40

    for history in self.deposit_history_list:
      print("-" * max_width)
      for key, value in history.items():
        print(f"| {key.ljust(7)}: {value.ljust(max_width - 16)}|")
      print("-" * max_width)
  
  # Q10. 출금 내역 정보 출력
  def withdraw_history(self):
    max_width = 40

    for history in self.withdraw_history_list:
      print("-" * max_width)
      for key, value in history.items():
        print(f"| {key.ljust(7)}: {value.ljust(max_width - 16)}|")
      print("-" * max_width)

    
# Q8. 3개 이상 인스턴스 생성
account_lee = Account('이종현',10)
account_jobs = Account('잡스',1000000000000)
account_adam = Account('애덤 그랜트',300000000000)

# Q8. 생성된 인스턴스 리스트에 담기
account_list = [account_lee, account_jobs, account_adam]

# Q9. 특정 잔고 이상 가지고 있는 고객 출력 메서드 선언
def get_more_balance_depositor_info(balance): 
  for depositor in account_list:
    if depositor.balance >= balance:
      depositor.display_info()

# Q9. 100만원 이상 잔고를 가지고 있는 고객 정보 출력
get_more_balance_depositor_info(1000000)

# Q10. 입금과 출금 내역 호출
account_lee.deposit(10000000000000)
account_lee.deposit(10000000000000)
account_lee.withdraw(10000000000000)
account_lee.withdraw(10000000000000)
account_lee.deposit_history()
account_lee.withdraw_history()
