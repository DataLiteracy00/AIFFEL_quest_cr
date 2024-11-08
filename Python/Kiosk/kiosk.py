# 사각형 넓이를 구하는 클래스 완성!
class Square:
    def __init__(self):
        self.square = int(input('넓이를 구하고 싶은 사각형의 숫자를 써주세요.\n 1.직사각형 2.평행사변형 3.사다리꼴 \n >>>'))

        if self.square == 1:
            print('직사각형 함수는 rect()입니다.')

        elif self.square == 2:
            print('평행사변형 함수는 par()입니다.')
        
        elif self.square == 3:
            print('사다리꼴 함수는 trape()입니다.')
        
        else:
            print('1, 2, 3 중에서 다시 입력해주세요')

    def rect(self):
        width, vertical = map(int, input('가로, 세로를 입력하세요. 예시 : 가로,세로\n >>>').split(','))
        area = width * vertical
        result = print('직사각형의 넓이는 : ' + str(area))
        return result

    def par(self):
        bottom, height = map(int, input("밑변과 높이를 입력해주세요. 예시 : 밑변,높이 ").split(","))
        area = bottom * height
        result = print('평행사변형의 넓이는 : ' + str(area))
        return result

    def trape(self):
        top, bottom, height = map(int, input("윗변과 밑변과 높이를 입력해주세요. 예시 윗변,밑변,높이 ").split(","))
        area = (top + bottom) * height / 2
        result = print('사다리꼴의 넓이는 : ' + str(area))
        return result

a = Square()
a.rect()

class Kiosk: 
    # 문제 2-1의 답을 입력하세요.     
    def __init__(self):
        self.menu = ['americano', 'latte', 'mocha', 'yuza_tea', 'green_tea', 'choco_latte']
        self.price = [2000, 3000, 3000, 2500, 2500, 3000]
        self.order_menu = []  # 주문 리스트
        self.order_price = []  # 가격 리스트

    # 메뉴 출력 메서드
    def menu_print(self):
        for i in range(len(self.menu)):
            print(i+1, self.menu[i], ' : ', self.price[i], '원')

    # 주문 메서드
    def menu_select(self):
        n = 0
        while n < 1 or len(self.menu) < n:
            n = int(input("음료를 번호를 입력하세요 : "))  # 음료 번호 입력

            # 메뉴판에 있는 음료 번호일 때
            if 1 <= n & n <= len(self.menu):
                self.order_price.append(self.price[n-1])  # 가격 리스트에 추가합니다.
                self.price_sum = self.price[n-1]  # 합계 금액

                # 메뉴판에 없는 번호일 때
            else:  
                print("없는 메뉴입니다. 다시 주문해 주세요.")


        # 음료 온도 물어보기
        t = 0  # 기본값을 넣어주고
        while t != 1 and t != 2:  # 1이나 2를 입력할 때까지 물어보기
            t= int(input("HOT 음료는 1을, ICE 음료는 2를 입력하세요 : "))
            # 문제 2-3의 답을 입력하세요. 
            if t == 1:
                    self.temp = "HOT"
            elif t == 2:
                self.temp = "ICE"
            else:    
                print("1과 2 중 하나를 입력하세요.\n")

        self.order_menu.append(self.temp + ' ' + self.menu[n-1])  # 주문 리스트에 추가합니다.
        # 문제 2-2의 답을 입력하세요. 
        print(f"{self.temp}, {self.menu[n-1]} : {self.price[n-1]} 원")

        # 추가 주문 또는 지불
        while n != 0:  # 지불을 선택하기 전까지 반복합니다.
            print()  # 줄 바꾸면서 
            n = int(input("추가 주문은 음료 번호를, 지불은 0을 누르세요 : "))  # 추가 주문 또는 지불
            if n > 0 and n < len(self.menu) + 1: 
                # 추가 음료 온도 
                # 문제 2-4. 추가 음료의 온도를 입력받고, 가격 리스트, 주문 리스트, 합계 금액을 업데이트해보세요.
                t= int(input("HOT 음료는 1을, ICE 음료는 2를 입력하세요 : "))

                if t == 1:
                    self.temp = "HOT"
                elif t == 2:
                    self.temp = "ICE"
                else:    
                    print("1과 2 중 하나를 입력하세요.\n")

                self.order_menu.append(self.temp + ' ' + self.menu[n-1])
                self.order_price.append(self.price[n-1])
                self.price_sum += self.price[n-1]

                print(f"추가 주문 음료, {self.temp} {self.menu[n-1]} : {self.price[n-1]}원\n 합계 : {self.price[n-1]}원")
            else :
                if n == 0 :  # 지불을 입력하면
                    print("주문이 완료되었습니다.")
                    print(self.order_menu, self.order_price)  # 확인을 위한 리스트를 출력합니다.
                else :  # 없는 번호를 입력할 때
                    print("없는 메뉴입니다. 다시 주문해 주세요.")

    # 지불 방법 선택            
    def pay(method):
        method = input("지불 방법을 선택해주세요. (현금 - cash or 1, 카드 - card or 2) ")

        if method == 'cash' or method == '1':
            print("직원을 호출하겠습니다.")
        elif method == 'card' or  method == '2':
            print("IC칩 방향에 맞게 카드를 꽂아주세요.")

    # 주문서 출력
    def table(self):
        print('⟝' + '-' * 30 + '⟞')
        for i in range(5):
            print('|' + ' ' * 31 + '|')

        for i in range(len(self.order_menu)):
            print(self.order_menu[i], ' : ', self.order_price[i])

        print('합계 금액 :', sum(self.order_price))

        for i in range(5):
            print('|' + ' ' * 31+ '|')
        print('⟝' + '-' * 30 + '⟞')


kiosk = Kiosk()  
kiosk.menu_print()  
kiosk.menu_select()  
kiosk.pay()  
kiosk.table()  