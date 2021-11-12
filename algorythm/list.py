score=[]
sc=0
print("점수를 입력하세요. 0인 경우 종료")
while True:
    sc=int(input("점수:"))
    if sc==0:
        break
    score.append(sc)
print("현재 입력된 점수는")
print(score,"이고, 모두",len(score),"개입니다.")

select=0
idx, val, cnt=0,0,0
while True:
    print("리스트 연습")
    print("0.exit")
    print("1.insert")
    print("2.sort")
    print("3.reverse")
    print("4.index")
    print("5.remove")
    print("6.del")
    print("7.count")
    select=int(input("원하는 번호를 선택하세요:"))
    if select==0:
        break
    elif select==1:
        idx=int(input("insert할 위치:"))
        val=int(input("insert할 값:"))
        score.insert(idx,val)
        print(score)
    elif select==2:
        score.sort()
        print(score)
    elif select==3:
        score.reverse()
        print(score)
    elif select==4:
        val=int(input("찾고 싶은 값:"))
        idx=score.index(val)
        print(score)
        print("%d는 %d번째 위치하고 있습니다." %(val, idx))
    elif select==5:
        val=int(input("삭제하고 싶은 값:"))
        score.remove(val)
        print(score)
    elif select==6:
        idx=int(input("삭제하고 싶은 위치:"))
        del(score[idx])
        print(score)
    elif select==7:
        val=int(input("개수를 알고 싶은 값:"))
        cnt=score.count(val)
        print(score)
        print("%d는 %d번 나옵니다." %(val,cnt))
        