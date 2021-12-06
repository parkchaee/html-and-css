#include <stdio.h>
//arr의 sum 구하기
//arr의 원소로 먼저 숫자 지정
int main(void){
    int arr[5];
    int sum=0,i;
    arr[0]=10, arr[1]=20, arr[2]=30, arr[3]=40, arr[4]=50;
    for (i=0; i<5; i++)
        sum+=arr[i];
    printf("배열 요소에 저장된 값의 합:%d\n",sum);
    return 0;
}
//각 배열 선정
//배열의 길이 알아보기
//길이를 이용해 원소 출력 
int main2(void){
    int arr1[5]={1,2,3,4,5};
    int arr2[]={1,2,3,4,5,6,7};
    int arr3[5]={1,2};
    int len1, len2, len3,i;
    //여기서 arr1의 크기는 바이트 기준
    printf("arr1의 크기 %d\n",sizeof(arr1));
    printf("arr2의 크기 %d\n",sizeof(arr2));
    printf("arr3의 크기 %d\n",sizeof(arr3));
    len1=sizeof(arr1)/sizeof(int); //배열 arr1의 길이 계산
    len2=sizeof(arr2)/sizeof(int);
    len3=sizeof(arr3)/sizeof(int);
    for (i=0; i<len1; i++){
        printf("%d",arr1[i]);
    }
    printf("\n")
    for(i=0 i<len2; i++)
    {
        printf("%d",arr2[i]);
    }
    printf("\n");
    for(i=0; i<len3; i++)
    {
        printf("%d",arr3[i])
    }
    printf("\n")
    return 0;
}
//널 문자는 문자열의 끝, 메모리 상에 값 0으로 저장
int nul(void){
    char str[]="good morning";
    printf("str 크기 %d\n",sizeof(str));//14이므로 인덱스 상 13
    printf("널 문자 문자형 출력:%c\n",str[13]); //없
    printf("널 문자 정수형 출력:%c\n",str[13]);
    str[12]="?"; //배열 속 수정 가능
    printf("%s",str);
    return 0;
}
//널, 공백 문자 비교(공백문자는 0이 아님)
int nulblank(void){
    char nu="\0";
    char bl=" ";
    printf("%c %c",nu,bl); //없
    printf("%d %d",nu,bl); //아스키 코드 0, 32
    return 0;
}
//문자열 받고 널 전까지 문자 출력
int scann(void){
    char str[50];
    int i=0;
    printf("문자열 입력");
    scanf_s("%s",str); //문자열 저장
    //배열의 경우 이미 첫번째 요소 주소를 가리키는 역할
    //따라서 &을 쓰지 않음
    //쓰고 싶다면 scanf_s("%s",&str[0]);
    printf("입력받은 문자열: %s\n",str);
    printf("문자 단위 출력");
    while(str[i]!="\0")
    {
        printf("%c",str[i]);
        i++;
        }
    printf("\n");
    return 0;
}
//배열의 끝은 문자열의 끝이 아님
//널 문자는 문자열의 끝을 판단할 수 있는 방법
int nul2(void){
    //scanf로 띄어쓰기 포함이 안될 뿐
    //char 배열 자체로 가능
    char str[50]="i like c programming";
    printf("string:%s\n",str);
    str[8]="\0"; //9번째 요소에 널 문자 저장
    printf("string: %s\n",str);
    //i like c까지 출력됨
    return 0;
}

int scann2(void){
    char str[50];
    int idx=0;
    printf("문자열 입력"); // He is my friend
    scanf_s("%s",str); //문자열을 입력받아 str에 저장
    //이때 공백을 기준으로 데이터 구분
    //따라서 공백 개수를 미리 알고 있지 않으면 공백 포함 문자열은 처리 불가
    printf("입력받은 문자열:%s\n",str);//He
    printf("문자 단위 출력"); //He
    while(str[idx]!="\n"){
        printf("%c",str[idx]);
        idx++;
    }
    printf("\n");
    return 0;
}

//2차원 배열의 선언
int arr2(void){
    int arr[3][4]; //3X4 matrix 
    arr[0][0]=1;//1행 1열
    //일반적으로 arr[N-1][M-1]=20;으로 정의
    //N행 M열 
    //행 : 가로 열 : 세로
    int arr1[7][9];
    printf("세로 3, 가로 4:%d\n",sizeof(arr1));
    return 0;
}
//아파트의 층 호수로 인구수 배정
//같은 층별 총 인구수 출력
int dep(void){
    int villa[4][2];
    int popu,i,j;
    for(i=0;i<4;i++)
    {
        for(j=0;j<2;j++){
            printf("%d층 %d호 인구수 ",i+1,j+1);
            scanf_s("%d",&villa[i][j]);
        }
    }
    for(i=0;i<4;i++){
        popu=0;
        popu+=villa[i][0]; //입력받은 인구수 대로
        popu+=villa[i][1];
        printf("%d층 인구수:%d\n",i+1,popu);
    }
    return 0;
}
//실제 메모리에는 1차원 형태로 주소값 지정
int po(void){
    int arr[3][2];
    int i,j;
    for(i=0;i<3;i++){
        for(j=0;j<2;j++)
        {
            printf("%p\n",&arr[i][j]);
            //포인터의 경우 print시 &
        }
    }
    return 0;
}
//2차원 배열
int arr2name(void){
    int arr[3][3]{
        {1,2,3},
        {4,5,6},
        {7} //빈칸은 0으로

    };
    int arr2[3][3]={1,2,3,4,5,6};
    return 0;

}
int arr2name2(void){
    int arr[3][3]={
        {1,2,3}
        {2,4,3}
        {3}
    };
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            printf("%d",arr[i][j]);

        }
        printf("\n");
    }
    printf("\n");
    return 0;
}
//3차원 배열 속에서 평균 배정하기 
int arr3(void){
    int mean=0;
    int arr[3][3][2]={
        {70,60},
        {40,50},
        {65,44}
    },
    {
        {46,55},
        {5,4},
        {3,6}
    },
    {
        {54,33},
        {22,4},
        {2,4}
    };
    for(int i=0;i<3;i++){
        for(int j=0;j<2;j++){
            mean+=arr[0][i][j];
        }
    }
    printf("%g\n",(double)mean/6);

    mean=0;
    for(int i=0;i<3;i++){
        for(int j=0;j<2;j++){
            mean+=arr[1][i][j];
        }
    }
    printf("%g\n",(double)mean/6);
     mean=0;
    for(int i=0;i<3;i++){
        for(int j=0;j<2;j++){
            mean+=arr[2][i][j];
        }
    }
    printf("%g\n",(double)mean/6);
    return 0;
}
