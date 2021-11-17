list = ["라이언킹", "말레피센트", "101마리의 달마시안 개"]
lion = ["첫번째 힌트 : 주인공의 아버지가 음모로 죽으며 이야기가 시작돼",
           "두번째 힌트 : 주인공은 결말에 왕이 된다",
           "세번째 힌트 : 주인공은 동물 중 사자야",
           "네번째 힌트 : 주인공의 이름의 초성은 ㅅㅂ",
           "네번째 힌트 : 작품의 초성은 ㄹㅇㅇㅋ이야"]

mali = ["첫번째 힌트 : 주인공은 날개를 가지고 있어",
          "두번째 힌트 : 그리고 머리에는 뿔이 있다!",
          "세번째 힌트 : 주인공은 인간에게 배신을 당한대!",
          "네번째 힌트 : 그 사람의 이름의 초성은 ㅁㄹㅍㅅㅌ ",
          "다섯번째 힌트 :잠자는 숲속의 공주를 원작으로 한다?"]

dalm = ["첫번째 힌트 : 주인공이 자식들을 잃어버리며 이야기가 시작된다",
        "두번째 힌트 : 주인공의 몸에는 검은 점이 있어!",
        "세번째 힌트 : 그리고 동물 중 개야",
        "네번째 힌트 : 이 영화는 크루엘라의 원작이라는데?",
        "다섯번째 힌트 : 주인공의 자식은 101마리야"]

point1 = 0
print("1번 문제\n")
for i in range(1, 6):
    print(lion[i-1])
    answer = input("정답을 입력하세요: ")
    if answer == lion[0]:
        print("\n정답입니다. 다음 문제로 넘어갑니다.")
        point1 = point1 + (6 - i)
        break
    else:
        print("오답입니다.\n")
        continue
        
print("1번 문제에서 ", point1, "점을 획득하였습니다.")

point2 = 0
print("\n\n2번 문제\n")
for i in range(1, 6):
    print(mali[i-1])
    answer = input("정답을 입력하세요: ")
    if answer == mali[1]:
        print("\n정답입니다. 다음 문제로 넘어갑니다.")
        point2 = point2 + (6 - i)
        break
    else:
        print("오답입니다.\n")
        continue
        
print("2번 문제에서 ", point2, "점을 획득하였습니다.")

point3 = 0
print("\n\n3번 문제\n")
for i in range(1, 6):
    print(dalm[i-1])
    answer = input("정답을 입력하세요: ")
    if answer == dalm[2]:
        print("\n정답입니다.")
        point3 = point3 + (6 - i)
        break
    else:
        print("오답입니다.\n")
        continue
        
print("3번 문제에서 ", point3, "점을 획득하였습니다.")

sum = point1 + point2 + point3
print("\n총 점수는", sum, "점 입니다.")

if (sum >= 13) :
    print("당신은 디즈니 세계의 수호자!")
elif sum >= 9 :
    print("~~~~~")