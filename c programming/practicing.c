#include <stdio.h>
int see(void){
    int num=10;
    int *ptr1=&num;
    int *ptr2=ptr1;
    (*ptr1)++; //num++
    (*ptr2)++; //num++
}

int pra(void){
    int num1=10;
    int num2=20;
    int *ptr1=&num1;
    int *ptr2=&num2;
    int temp;
    *ptr1+=10; //(*ptr1)+=10;과 차이없음(우선순위 구별)
    temp=ptr1;
    *ptr2-=10;
    ptr1=ptr2; //num 대신이 아니라 주소 저장이라

    ptr2=temp;
}
int pl2(void){
    int arr[5]={1,2,3};
    int *ptr=arr;
    for(int i=0;i<5;i++){
        *ptr+=2;
        ptr++;
    }
}
int pl3(void){
    int arr[5]={1};
    int *ptr=arr;
    for(int i=0;i<5;i++){
        *(ptr+i)+=2;
        
    }
}
int sum(void){
    int s=0;
    int arr[]={1,1,2};
    int*ptr=arr;
    for(int i=0;i<5;i++){
        s=*(ptr--);
        /*
        s=*ptr;
        ptr--;
        */
    }
}
int back(void){
    int arr[6]={2,3};
    int *ptr=arr;
    int *ptr2=arr[5];
    int temp;
    for(int i=0;i<3;i++){
        temp=*ptr;
        *ptr=*ptr2;
        *ptr2=temp;
        ptr++;
        ptr2--;
    }
}