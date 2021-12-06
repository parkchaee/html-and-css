int str(void){
    int ch1,ch2;
    ch1=getchar();//문자 입력
    ch2=fgetc(stdin);//엔터 키 입력
    putchar(ch1); //문자 출력
    fputc(ch2,stdout); //엔터 키 출력
    //fputc 또는 putc는 데이터의 맨 앞 문자만 출력
    return 0;
}
int str2(void){
    int ch;
    while(1){
        ch=getchar();
        if(ch==EOF){
            //EOF는 파일의 끝을 표현하기 위한 상수 :-1
            break;
        }
        putchar(ch);
    }
    return 0;

}
int convCase(int ch{
    const int diff='a'-'A';
    if(ch>='A' && cha<='Z'){
        return ch+diff;
    }
    else if (ch>='a'&&ch<='z'){
        return ch-diff;
    }
    else{
        return -1;
    }
}
int main(void){
    int ch;
    printf("Input>");
    ch=getchar();
    ch=convCase(ch);
    if (ch==-1){
        puts("범위를 벗어난 입력입니다");
        return -1;
    }
    putchar(ch);
    return 0;
}