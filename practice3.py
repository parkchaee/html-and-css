#d=정수

print("나는 %d살입니다." % 20)
#s=string
print("나는 %s을 좋아해요." % "파이썬")
#c=character=1글자
print("apple은 %c로 시작해요." % "a")
#%s

print("%s살" % 20)
print("나는 %s,%s색" % ("빨간", "파란"))

print("나는 {}살".format(20))
print("나는 {},{}색".format("파란","빨간"))
print("나는 {0},{1}색".format("파란", "빨간"))

#0, 1의 기준은 파란, 빨간의 순서 
#ex){1},{0}으로 순서 변환 가능
print("나는 {age},{color}".format(age = 20,color="빨강"))
#color과 age의 정의의 순서는 상관없음

age=20
color="빨간"
print(f"나는 {age}, {color}")

#탈출 문자 

#1. \n 문장 내 줄 바꿈 이후 출력
print("백무니 불여일견 \n백견이 불여일타")
#문장 안의 ""
print("저는 \"나도\"입니다.")
#"저는 '나도'입니다" 의 방법도 있음
#2. \\: 문장 내에 \ 1개 url
print("c:\\")
#3. \r :커서를 맨 앞으로 이동
print("red apple/rpine")
#red apple-> pineapple 
#맨 앞으로 커서를 이동하게 된 이후 남은 수만큼 교환
#4. \b:backspace, one character delete
#5. \t : tab = 4 space
print("red\tapple")

'''사이트별로 비밀번호를 만들어주는 프로그램
http://naver.com
1. http://은 제외 
2. 처음 만나는 점(.) 이후 부분 제외
3. 남은 글자 중 처음 3자리, 글자 개수, 글자 내 e 갯수,
"!"로 구성'''

#slice 대체- list[2:4]=[42,42]

pin="http://naver.com"
pin2=pin.replace("http://","")
num=pin2.find(".")
pin3=pin2.replace(pin2[num:],"")
print(pin3[:3]+str(len(pin3))+str(pin.count("e"))+"!")

url = "http://naver.com"
my_str=url.replace("http://","")
my_str=my_str[:my_str.index(".")] #. 직전까지 재지정
#somethin=my_str.find(".")
#my_str=my_str[:somethin]--> 한번에 [:my_str.index(".")]로 간추림
password=my_str[:3]+str(len(my_str))+str(my_str.count("e")+"!")
print("{0}의 비밀번호는 {1}입니다.".format(url, password))
