btschars={"진":"RJ", "슈가":"Shooky","제이홉":"Mang","RM":"Koya","지민":"Chimmy","뷔":"Tata","정국":"Cooky"}
while True:
    myBTS=input(str(list(btschars.keys()))
    +"중 좋아하는 멤버는?")
    if myBTS in btschars:
        print("<%s>의 캐릭터 인형은 <%s>입니다." %(myBTS,btschars[myBTS]))
    elif myBTS=="끝":
        break
    else:
        print("BTS에는 그런 멤버가 없습니다. 확인해보세요.") 

