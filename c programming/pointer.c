                             #include <stdio.h>
int purpose(void){
    char ch1="A", ch2="Q";
    int num=7;
    //정수 형태의 주소값 저장
}
int poin(void){
    int num=7;
    int *pnum; //int*형 변수의 주소값을 저장하는 포인터 변수 pnum선언
    pnum=&num; //num의 주소값을 pnum에 저장
}
void size(void){
    int num=0;
    int *x=&num;
    //포인터 변수의 크기는 시스템의 주소 값 크기에 따라 달라짐
    //32비트 시스템- 주소값 크기 32비트- 포인터 변수의 크기 32비트
    printf("%zu",sizeof(x)); 
    //%zu는 size_t형 값 출력
    //이는 시스템 별 다른 객체의 최고 크기를 저장하는 자료형 
}
int var(void){
    int *
    int * pnum1; //int 형 포인터 변수 pnum1
    double *
    double *pnum2; 
    //포인터가 가리키는 변수의 형에 따라 달라짐
    //type 과 관계없이 포인터 변수에는 주소값만 저장
    type* //type형 포인터
    type*ptr; //type형 포인터 변수 ptr

}
int and(void){
    int num=5;
    int *pnum=&num;
    //&연산자는 변수의 주소값 반환 
    //int형 num 변수의 주소값 (&num)을 int*형 포인터 변수 pnum에 저장

}
/*int typee(void){
    int num1=5;
    double*pnum1=&num1; //일치하지 않음
}*/
int star(void){
    int num=10;
    int*pnum=&num;
    *pnum=20; //pnum이 가리키는 공간에 20 저장 
    //*pnum은 num 의미 
    //num을 놓을 자리에 *pnum 놓음
    printf("%d",*pnum);
}
int yoen(void){
    int num1=100, num2=100;
    int *pnum;
    pnum=&num1;
    (*pnum)+=30;
    printf("%d\n",num1);
    return 0;
}
//포인터 형은 메모리 공간을 참조하는 방법의 힌트
int wrong(void){
    int *ptr;
    *ptr=10; //ptr은 상수값으로 초기화하지 않음
    int *ptr=125; //마찬가지 

}
//널 포인터를 이용한 초기화 
int nul(void){
    int*ptr=0;
    int *ptr2=NULL; //숫자 0을 의미 
    //아무것도 가리키지 않음
    //잘못된 연산을 막기 위해 널 포인터로 초기화 

}
//배열의 이름= 배열의 시작 주소값을 의미하는 포인터
//배열의 첫번째 요소를 가리킴
//대입 연산 불가능 
int arr(void){
    int arr[3]={0,1,2};
    printf("배열의 이름:%p\n",arr);
    printf("첫번째 요소:%p\n",&arr[0]);
    printf("두번째 요소:%p\n",&arr[1]);
    printf("세번째 요소:%p\n",&arr[2]);
    //arr=&arr[i]; // 이 문장은 컴파일 에러를 일으킴
    return 0;
}
int main(void){
    int arr1[3]={1,2,3};
    double arr[3]={1.1,2.2,3.3};
    printf("%d %g\n",*arr1,*arr2);
    *arr1+=100;
    *arr2+=120.5;
    printf("%d %g\n",arr1[0],arr2[0]); //101,121.6
    return 0;
}
//arr은 int 형 포인터와 동일하므로
//int 형 포인터를 대상으로 배열 접근을 위한 [idx] 연산을 진행한 것과 동일
int name(void){
    int arr[3]={1,2,3};
    arr[0]+=5;
    arr[1]+=7;
    arr[2]+=9;

}
int name2(void){
    int arr[3]={15,25,35};
    int*ptr=&arr[0]; //int *ptr=arr;과 동일한 문장
    printf("%d %d\n",ptr[0],arr[0]); //같
    printf("%d %d\n",ptr[1],arr[1]); //같 (25)
    return 0;
}
int plm2(void){
    int arr[3]={11,22,33};
    int*ptr=arr;//int *ptr=&arr[0];과 같은 문장
    printf("%d %d %d\n",*ptr,*(ptr+1),*(ptr+2));
    printf("%d",*ptr); ptr++; //printf 함수 호출 후 ptr++실행
    //11 22 33
    //11 22 33 11 의 연산 결과
    //ptr이 ++됨에 따라 다음 위치로 넘어감 - 11이 출력
}
//포인터 변수를 이용한 배열의 접근 방식을 배열의 이름에도 사용
//배열의 이름을 이용한 접근방식을 포인터 변수 대상 이용
//arr이 포인터의 변수 or 배열의 이름이건 arr[i]==*(arr+i)
int arrpoin(void){
    int arr[3]={11,22,33}
    int *ptr=arr;
    printf("%d %d %d\n",*ptr,*(ptr+1),*(ptr+2));
    printf("%d %d %d\n",*(ptr+0),*(ptr+1),*(ptr+2)); //*(ptr+0)는 *ptr
    printf("%d %d %d\n",ptr[0],ptr[1],ptr[2]);
    printf("%d %d %d\n",*(arr+0),*(arr+1),*(arr+2));
    printf("%d %d %d\n",arr[0],arr[1],arr[2]);
    return 0;
}