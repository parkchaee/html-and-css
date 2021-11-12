import random
secretLen=3
secretList=random.sample(range(10),secretLen)
secret=' '
for i in range(secretLen):
    secret+=str(secretList[i])
print(secret)
for  chance in range(10,0,-1):
    while True:
        guess=input(("you have %d chane(s)"%chance)+"guess my three digit-num")

        if len(guess)==secretLen and guess.isdigit():
            break
        print(guess)
        
        strike=0
        ball=0
        for i in range(secretLen):
            if secret[i]==guess[i]:
                strike+=1
            elif secret[i] in guess:
                ball+=1
        print(secret,strike,ball)

        if strike==secretLen:
            print("you guessed my num")
            break
        if strike>0:
            if ball>0:
                print("%d strikes and %d balls\n"%(strike,ball))
            else:
                print("%d strikes\n"%strike)
            