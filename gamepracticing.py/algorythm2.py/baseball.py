#숫자 야구 게임
#랜덤한 3~6자리 수를 추론하는 게임
#0~9 중 3개 랜덤 선택
#strike: 비밀 숫자와 추론 숫자 내 값과 위치 same
#ball: 비밀 숫자, 추론 숫자 내 값만 같고 위치 dif 
#out: 비밀 숫자, 추론 숫자 내 값이 dif
import random
secretLen=3
secretList=random.sample(range(10),secretLen) #0~9중 3개 랜덤 선택
secret=''
for i in range(secretLen):
    secret+=str(secretList[i]) #문자열로 변환 !!!
for chance in range(10,0,-1): #10번의 기회 
    while True:
        #추론 숫자 입력
        guess=input(("You have %d chance(s)."%chance)+ "Guess my three-digit number:")
        if len(guess)==secretLen and guess.isdigit(): #올바른 입력 시 중단
            break
        #str.isdigit() 문자열이 숫자로만 이루어져있는가 
        #추론 숫자 분석
        strike=0
        ball=0
        for i in range(secretLen):
            if secret[i]==guess[i]:
                strike+=1
            elif secret[i] in guess:
                ball+=1
        print(secret, strike, ball)

        #분석 결과 출력 !!!
        if strike == secretLen: #모든 원소+위치를 맞춘 것이므로 
            print("You guessed my number!!")
            break
        if strike>0:
            if ball>0:
                print("%d strike(s) and %d ball(s)\n"%(strike,ball))
            else:
                print("%d strike(s)\n" %strike)
        else:
            if ball>0:
                print("%d ball(s)\n"%ball)
            else:
                print("Out\n")
                print(" you failed to guess my number..")

    print(guess) 
