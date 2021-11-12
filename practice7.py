#function defining
def open_account():
    print("새 계좌 생성")
open_account() # 로 호출

#입금
#format(balance+money)
def deposit(balance, money):
    print("complete, total={0}".format(balance+money))
    return balance+money
balance=0
balance=deposit(balance, 1000)
print(balance)

#출금
def withdraw(balance, money):
    if balance>= money:
        print("complete, total {0}".format(balance-money))
        return balance-money
    
    else:
        print("failed, total{0}".format(balance))
        return balance
balance=0
balance=deposit(balance,1000)
balance=withdraw(balance,2000) 
#함수에서 계산을 한 이후에 실질적으로 balance 잔고의 값
#을 담고 있는 부분이 필요하므로 변수로 계속 저장시켜줌

def withdraw_night(balance, money):
    commission=100
    return commission, balance-money-commission
#튜플 형식으로 ,로 값을 구분해서 여러개의 값을 반환할 수 있
balance=0 #잔액
balance=deposit(balance,1000)
commission, balance=withdraw_night(balance, 500)
#<-commission 값도 보기 위해 
print("수수료{0}, 잔액{1}".format(commission, balance))

#함수에서 기본값 설정하기
def profile(name, age, lang):
    print("name:{0}\t age:{1}\t lang:{2}\t".format(name, age, lang))
profile("유재석",20,"파이썬")
#다른 방식으로 호출하기
#키워드 이용 + 순서 뒤죽박죽
#기본값으로 설정해넣기
profile(name="김태호", lang="python", age="20")

#같은 학교, 학년, 반, 수업
#매번 프로필에서 불필요한 설정 필요 x

def profilee(name, age=17, lang="파이썬"):
    print("name:{0},age:{1},lang:{2}".format(name, age, lang))
profilee("유재석")  #나이, 언어도 함께 뜸

#가변 인자를 이용한 함수 호출
def profileee(name, age, lang1, lang2, lang3):
    print("name:{0},age:{1}.".format(name, age), end=" ")
    print(lang1, lang2, lang3)
profileee("유재석", 20, "py","ja","c")

#print("", end" ") => 끝에 enter x 이므로 한줄에

#할 줄 아는 언어가 정의한 함수 자체보다 많거나 적은 경우
#새로운 함수를 지정해야하므로 가변인자 활용

def profileee(name, age, *language):
    print("name:{0},age:{1}.".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()
profileee("유재석", 20, "py","ja")
#print()는 줄바꿈용 / print 함수 자체로 쓴 것 
#부족할 경우 " " " " " " 으로 자릿수를 채워주지 않아도 됨


