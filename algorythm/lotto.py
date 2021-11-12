import random
lotto=[]
num=0
def getNumber():
    return random.randrange(1,46)
def PrintLotto(lot):
    for i in range(0,6):
        print("%d"%lot[i], end='')
print("**로또 추첨을 시작합니다.**\n")
while True:
    num=getNumber()
    if lotto.count(num)==0: 
    #지정된 무작위의 숫자가 list안에 없다면
    #if num not in lotto:

        lotto.append(num)
    if len(lotto)>=6:
        break
print("추첨된 로또 번호==>", end=' ')
lotto.sort()
for i in range(0,6):
    print("%d" %lotto[i], end=' ' )
