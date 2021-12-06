#include <stdio.h>
//11-1
//길이가 5인 int형 배열 선언
//5개의 정수 입력받기
//입력된 정수 중 최댓값, 최솟값, 총합
//반드시 입력을 완료한 상태에서 계산
int sum(void){
    int arr[5];
    int max,min,sum,i;
    for (int i=0;i<5;i++){
        printf("정수값 입력");
        scanf_s("%d",&arr[i]);
    }
    max=min=sum=arr[0];
    for (int i=1;i<5;i++){
        sum+=arr[i];

        if (arr[i]>max){
            max=arr[i];
        
        if (arr[i]<min){
            min=arr[i];
        }
    } 
   
    printf("%d ", max);

}

int word(void){
    char arr[]={"G","o","o","d"," ", "t", "i","m","e"};
    int i;
    for(i=0; i<sizeof(arr)/sizeof(char);i++){
        //i<sizeof(arr)
        printf("%c",arr[i]);

    }
    printf("\n");
    return 0;
}
/* 문자열의 경우 입력 및 출력의 과정
int nul(void){
    char str[]="good morning";
    printf("str 크기 %d\n",sizeof(str));//14이므로 인덱스 상 13
    printf("널 문자 문자형 출력:%c\n",str[13]); //없
    printf("널 문자 정수형 출력:%c\n",str[13]);
    str[12]="?"; //배열 속 수정 가능
    printf("%s",str);
    return 0;
}
*/
//str의 경우만 len=sizeof(str)/sizeof(char)아니고
//len=sizeof(str) 인가 봄

//11-2 입력받은 영단어의 길이 출력
int wordlen(void){
    char voca[];
    int lens=0;
    scanf_s("%s",voca);
    while(voca[lens]!="\0"){
        len++;
    }
    printf("길이=%d",lens);
   return 0;
}
//영단어 입력받아 char형 배열 저장
//역순으로 뒤집고 출력
//널 위치 변경 불가
int wordbw(void){
    char word[100],temp;
    int i,lens;
    int i=lens=0;
    scanf_s("%s",word);
    while(word[lens]!="\0"){
        lens++;
    }
    
    for(int i=0;i<lens/2;i++){
        temp=word[i];
        word[i]=word[lens-1-i];
        word[lens-1-i]=temp;
    }
    printf("뒤집힌 영단어 %s",word);
}
//입력받은 영단어 중 아스키 코드 값이 가장 큰 문자
int asc(void){
    int len=0,i;
    char voca[100];
    printf("영단어 입력");
    scanf_s("%s",voca);
    while(voca[len]!="\0"){
        len++;
    }
    max=voca[0];
    for(i=1;i<len;i++){
        if (max<voca[i]){
            max=voca[i];
        }
    }
    printf("%c\n",max);
    return 0;
}
//가로 길이 9 세로 3인 2차원 배열
//2,3,4단 저장
int gugu(void){
    int arr[3][9],i,j;
    for(i=0;i<3;i++){
        for(j=0;j<9;j++){
            arr[i][j]=(i+2)*(j+1);
        }
    }
    for(i=0;i<3;i++){
        for(j=0;j<9;j++){
            printf("%2d",arr[i][j]);
        }
        printf("\n");
    }
    return 0;
}
//배열 A 2x4
//배열 B는 4x2로 A이용
int trans(void){
    int aarr[2][4];
    int barr[4][2];
    int aarr={
        {1,2,3,4},
        {5,6,7,8}
    };
    for(int i=0;i<2;i++){
        for(int j=0;j<4;j++){
            barr[j][i]=aarr[i][j];
        }
    }
    for(i=0;i<4;i++){
        for(j=0;j<2;j++){
            printf("%d",barr[i][j]);
        }
        printf("\n")
    }
    return 0;
}