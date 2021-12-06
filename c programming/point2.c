#include <stdio.h>
int main(void){
    char str1[]="My String";
    //포인터 상수:포인터 변수가 가리키고 있는 주소 값을 변경할 수 없
    str1[0]="x"; //문자열 내부의 문자 변경 가능 
    char*str2="Your String";//Your String\0 
    //상수를 가리키는 포인터:새 지정 가능 
    str="Our team"; 
}
int numarr(void){
    int num1=10,num2=20,num3=30;
    //변수의 자료형을 표시하는 부분 마지막에 *추가 
    int*arr[3]={&num1,&num2,&num3};
    //변수들의 배열이므로 & 연산자 필요 
    //길이가 3인 int형 포인터 배열 arr
    //포인터가 요소로 구성되는 배열 
    printf("%d\n",*arr[0]);
    printf("%d\n",*arr[1]);
    return 0;
}
int strarr(void){
    char *strarr[3]={"simple","string","array"};
    //변수 지정 이후 배열로 넣은 게 아니므로 &연산자 x 
    printf("%s\n",strarr[0]); 
    printf("%s\n",strarr[1]);
    return 0;
}
//배열을 함수의 인자로 전달하는 예
//배열의 모든 값이 아닌 주소값이 복사되어 매개변수로 복사
//배열이 매개변수인 경우 직관적으로 배열을 의미하는 int param[]이 더 많이 사용
//그 외 영역에서 int *ptr 선언을 int ptr[]로 바꾸는 경우 불가

//call by address/pointer ->call by reference 와 유사한 구현

void arrfunc(int *param,int len){
    int i;
    for(i=0;i<len;i++){
        printf("%d",param[i]);
    }
    printf("\n");
}
int func(void){
    int arr1[3]={1,2,3};
    int arr2[5]={1,2,3,4,5};
    arrfunc(arr1,sizeof(arr1)/sizeof(int));
    arrfunc(arr2,sizeof(arr2)/sizeof(int));
    return 0;
}
void show(int *param,int len){
    for(int i=0;i<len;i++){
        printf("%d",param[i]);
    }
    printf("\n");
}
void add(int *param,int len,int add){
    for(int i=0;i<len;i++){
        param[i]+=add;
    }
}
int func2(void){
    int arr[3]={1,2,3};
    add(arr,sizeof(arr)/sizeof(int),1) //add->show이므로
    //따로 add에 printf가 필요하지 않음 
    show(arr,sizeof(arr)/sizeof(int));
    return 0;
}
//cbv 인자의 값이 복사되어 매개변수로 전달
//매개변수의 값 변경이 함수 외부에 영향 x
//잘못 적용된 call-by-value, 값복사 
void swap(int n1,int n2){
    int temp=n1;
    n1=n2;
    n2=temp;
    printf("n1 n2:%d %d\n",n1,n2);
}
//swap 함수 내부에서의 교환은 외부에 영향 x cbv 형태이므로
int cbv(void){
    int num1=10,num2=20;
    printf("num1 num2:%d %d\n",num1,num2);
    swap(num1,num2);
    printf("num1 num2:%d %d\n",num1,num2);
    return 0;
}
//올바르게 적용
void swap2(int *ptr1, int*ptr2){
    int temp=*ptr1;
    *ptr1=*ptr2;
    *ptr2=temp;
}
int cbv2(void){
    int num1=10,num2=20;
    printf("num1 num2:%d %d\n",num1,num2);
    swap2(&num1,&num2);
    printf("num1 num2:%d %d\n",num1,num2);
    return 0;
}
int sca(void){
    int num;
    scanf("%d",&num);
    //scanf는 외부 선언 변수에 접근하기 위한 주소값 필요
}
int str(void){
    char str[30];
    scanf("%s",str);
    //str은 배열 이름- 자체가 주소값- &가 필요 없음
}