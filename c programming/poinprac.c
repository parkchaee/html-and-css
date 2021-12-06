#include <stdio.h>
int see(void){
    int num=10;
    int *ptr1=&num;
    int *ptr2=ptr1;
    (*ptr1)++; //10+1=11
    (*ptr2)++; //*ptr2=ptr1=11, 11+1=12
    //ptr++;의 경우 배열에서 메모리 위치를 이동해감
    //이 경우 배정된 num에 대한 계산 
    printf("%d\n",num);
    return 0;
}
//두 변수 두 포인터로 각각 가리키기
//ptr1,ptr2 이용해 num1+10, num2-10으로 
//포인터가 가리키는 대상 바꾸기 
//변수에 저장된 값 출력
int pra(void){
    int num1=10;
    int num2=20;
    int *ptr1;
    int *ptr2;
    int temp;
    *ptr1=&num1;
    *ptr2=&num2;
    (*ptr1)+=10;
    (*ptr2)-=10;
    temp=ptr1;
    ptr1=ptr2;
    ptr2=temp;
    printf("%d %d\n",*ptr1,*ptr2);
}

//길이가 5 인 int형 arr선언 1,2,3,4,5로 초기화
//첫번째 요소 ptr로 선언, 이를 이용해 저장된 값 증가 +2
int pl2(void){
    int arr[5]={1,2,3,4,5};
    int *ptr=arr;
    for(int i=0;i<5;i++){
        *ptr+=2;
        ptr++;
    }
    for(i=0;i<5;i++){
        printf("%d",arr[i]);
    }
    printf("\n");
    return 0;
}
//ptr에 저장된 값을 변경시키지 않고
//ptr 대상 덧셈 연산
int pl3(void){
    int arr[5]={1,2,3,4,5};
    int *ptr=arr;
    for(int i=0;i<5;i++){
        *(ptr+i)+=2;
    }
    for(i=0;i<5;i++){
        printf("%d",arr[i]);
    }
    printf("\n")
    return 0;
}
//ptr 에 저장된 값 감소
//하는 형태로 모든 정수 더하기
int pl4(void){
    int arr[5]={1,2,3,4,5};
    int*ptr=arr[4];
    int tot=0;
    for(int i=0;i<5;i++){
        tot+=*(ptr--);
        /*
        s=*ptr;
        ptr--;
        */
    }
    
    printf("%d",tot);
}
//배열의 순서를 바꾸기
//두 포인터 선언 이용
int ba(void){
    int arr[6]={1,2,3,4,5,6};
    int *ptr1=arr[0];
    int *ptr2=arr[5];
    int temp;
    for(int i=0;i<3;i++){
        temp=*ptr1;
        *ptr1=*ptr2;
        *ptr2=temp;
        ptr1++;
        ptr2--;

    }
    for(i=0;i<6;i++){
        printf("%d",arr[i]);
    }
    printf("\n");
    return 0;
}