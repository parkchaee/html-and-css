while True:
    print("===============")
    print("===1.정수출력하기===")
    print("===2.짝수출력하기===")
    print("===3.홀수출력하기===")
    print("===4.배수출력하기===")
    print("===5.약수출력하기===")
    print("===6.그만하기=======")
    print("=================")

    menu=int(input("메뉴를 선택하세요"))
    if menu==6:
        print("프로그램을 끝냅니다")
        break
    if menu==1 or menu==2 or menu==3 or menu==4 or menu==5:
        loop=int(input("반복할 횟수를 입력하세요"))
        value=int(input("숫자를 입력하세요"))
        if menu==1:
            print("정수값 처리를 시작합니다")
            for x in range(1,loop+1,1):
                print(x,end=" ")
        elif menu==2:
            print("짝수값 처리를 시작합니다")
            for x in range(1,loop+1,1):
                if x%2==0:
                    print(x,end=" ")
        elif menu==3:
            print("홀수값 처리를 시작합니다")
            for x in range(1,loop+1,1):
                if x%2==1:
                    print(x,end=" ")
        elif menu==4:
            print("배수값 처리를 시작합니다")
            for x in range(1,loop+1,1):
                if x%value==0:
                    print(x,end=" ")
        else:
            print("약수값 처리를 시작합니다")
            for x in range(1,value+1,1):
                if value%x==0:
                    print(x,end=" ")

