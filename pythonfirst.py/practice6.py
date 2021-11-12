#직원이 이름을 부르고, 확인을 받음
#올때까지 반복
customer="thor"
person="unknown"
while person!=customer:
    print("{0}, coffee ready.".format(customer))
    person=input("name?")
#absent, no book, nothing 인 학생으로 나누기
#선생이 차례로 부르고 다른 반응 입히기 
absent=[2,5]
no_book=[7]
for student in range(1,11):
    if student in absent: #list 이므로 in
        continue
    elif student in no_book:
        print("{0}, punishment".format(student))
        break
    else:
        print("{0}, read".format(student)) # students, not absent
#absent 건너뛰고 continue

#출석 번호가 1~4, 앞에 100을 붙이기로 
#아예 원소를 변환시키기 
students=[1,2,3,4]
students=[i+100 for i in students]
print(students)
#학생 이름을 길이로 변환
studentss=["thor"]
studentss=[len(i) for i in studentss]
print(studentss)
#학생 이름을 대문자로
studentss=["thor"]
studentss=[i.upper() for i in studentss]

'''50명의 승객과 매칭 기회, 총 탑승 수 구하기
1. 승객별 운행 소요 시간은 5~50분 사이 난수
2. 소요시간 5~15분 사이 승객만 매칭
출력문 예제
[0] 1 번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
...
[ ] 50번째 손님 (소요시간 : 16분)
총 탑승 승객: 2분'''

count=0
on=0
from random import *
while count<50:
    count+=1
    time=randint(5,51)
    if 5<=time<=15: 
        on+=1
        print("[0] {0}번째 손님 (소요시간: {1}분".format(count,time))
    else:
        print("[ ] {0}번째 손님 (소요시간: {1}분)".format(count, time))
print("총 탑승 승객: {0}분".format(on))

#in range(5,16) 으로 확인해보기 => random이니까 할 때마다 
#답의 값은 바뀜
count=0
on=0
from random import *
while count<50:
    count+=1
    time=randint(5,51)
    if time in range(5,16):
        on+=1
        print("[0] {0}번째 손님 (소요시간: {1}분".format(count,time))
    else:
        print("[ ] {0}번째 손님 (소요시간: {1}분)".format(count, time))
print("총 탑승 승객: {0}분".format(on))

