#list
subway=[10,20,30]
print(subway)

a=['a']
if 'g' in a:
    a.remove('g') 
#error이 나지 않고 삭제
#전체 list 원소 출력
#\n이 내제되어있음
for i in a:
    print(i)

a=['a','b']
b=a[:] #b=a로 복사하는 것과 달리 통채로 복사하는 오랍른 형태
print(b)
b[1]='2' # 복사 이후 재정의가 가능함
subway=["유재석", "조세호", "박명수"]
#조세호가 타고 있는 칸
print(subway.index("조세호"))
#뒤로 추가
print(subway.append("하하"))
#좌석 지정 추가 : 1번째로 정형돈을 넣음
print(subway.insert(1,"정형돈"))
print(subway) #index 이외는 따로 print(subway) 해줘야 뜸
#뒤에서부터 하나씩 빼기
print(subway.pop())
# list에서 count 이용: 같은 이름인 사람의 명수 확인하기
subway.append("유재석")
print(subway.count("유재석"))
#정렬
num_list=[5,4,3]
print(num_list.sort())
#순서 뒤집기
print(num_list.reverse())
#모든 값을 지우기
print(num_list.clear())
#여러 자료형 함께 사용 가능 boolean 포함
#list의 확장
print(num_list.extend(subway))

#dictionary
cabinet={3:"유재석", "b100":"김태호"} #key: 3 value: 유재석
print(cabinet[3]) #[key]로 대가 확인
print(cabinet.get(3)) 
#[]는 오류로 종료가 됨, .get()의 경우 none 이후 넘어감
print(cabinet.get(5,"사용가능")) #없을 경우 "사용가능으로 대체"

print(3 in cabinet) # boolean으로 확인

cabinet["c-20"]="조세호" #값 정의, 새롭게 업데이트 가능
#이 상황에서 {} 가 아닌 []을 이용함 주의 

del cabinet["c-20"] #값 삭제

print(cabinet.keys()) #keys 출력
print(cabinet.values())
print(cabinet.items()) #key, values 출력

print(cabinet.clear()) #모두 삭제

#tuple
#소괄호 생략하고 정의 가능
#ex) tup=(10,20,30)
#tup=10,20,30 의 형태로
#전체 튜플을 지우는 것은 가능 
#1.변경되지 않는 list의 경우 속도가 더 빠르므로 사용
menu=("돈까스", "치즈까스")
print(menu[0])
#menu.add("생선까스")-> 값의 추가, 변경 불가능
#2. 한꺼번에 지정, 출력
name="김종국"
age=20
hobby="코딩"
print(name, age, hobby)

name, age, hobby=("김종국", 20, "코딩")
print(name, age, hobby)


#집합 = set
#중복 안되고 순서 없음
my_set={1,2,3,3,3} #{1,2,3}으로 무시됨
print(my_set)

java={"유재석","김태호"}
python=set(["유재석","박명수"])
#교집합 
print(java.intersection(python)) 
print(java & python)
#합집합
print(java|python)
print(java.union(python))
#차집합
print(java-python)
print(java.difference(python))
#python set에 추가
print(python.add("김태호")) 
'''none으로 뜨니까 add 이후 print 따로 해 줄 것'''
python.add("김태호")
print(python)
#제거
java.remove("김태호")
print(java)


''' 자료 구조
stack - 한쪽이 막혀있는 형태 
a-b-c--->c-b-a
=LIFO 
*데이터를 넣=push
빼는=pop
확인했다 넣는=peep
비어있는 위치=top

<->큐 - FIFO'''