#그냥 순서대로가 아니라 학번처럼 고유 번호가 
#배정되어있는 경우
def find_name(num,nolist,namelist):
    lens=len(nolist)
    result="?"
    for i in range(lens):
        if nolist[i]==num:
            result=namelist[i]
    return result

stu_no=[39,14,67,105,32,27,100]
stu_name=["진","슈가","제이홉","RM","지민","뷔","정국"]
while True:
    print(stu_no)
    a=int(input("학생번호를 입력하세요.(-1은 끝내기):"))
    if a!=-1:
        print(find_name(a,stu_no,stu_name))
    else:
        break