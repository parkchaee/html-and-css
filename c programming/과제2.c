#include <stdio.h>
#pragma warning(disable: 4996)

int main(void) {
    
    int num;
    int seat;
    char mun;
    int sum = 0;
    int num2;
    int res;
    char rarr[5][10];
    for (int i = 0;i < 5;i++) {
        for (int j = 0;j < 10;j++) {
            rarr[i][j]= '_';
        }
    }
    char sarr[5][10];
    for (int i = 0;i < 5;i++) {
        for (int j = 0;j < 10;j++) {
            sarr[i][j] = '_';
        }
    }
    rarr[0][5] = 'x';
    sarr[0][0] = 'x';
    sarr[0][1] = 'x'; 
    sarr[0][2] = 'x';
    sarr[0][3] = 'x';
    sarr[0][4] = 'x';
    
    while (1) {
        printf("==========================================================================================\n");
        printf("1.좌석 현황 출력, 2.예약, 3.예약 취소, 다른 값은 종료>");
        scanf("%d", &num);
        
        if(num == 1){
            printf("o: 귀하가 예약한 좌석, x: 타인이 예약한 좌석,_:빈 좌석입니다.\n");
            printf("R석\n");
            for (int i = 0;i < 5;i++) {
                for (int j = 0;j < 10;j++) {
                    printf("%c", rarr[i][j]);
                }
                printf("\n");
            }
            printf("\n");

            printf("S석\n");
            for (int i = 0;i < 5;i++) {
                for (int j = 0;j < 10;j++) {
                    printf("%c", sarr[i][j]);
                }
                printf("\n");
            }
            printf("\n");
        }
        else if (num == 2) {

            printf("R석은 5만원, S석은 3만원입니다.\n");
            printf("좌석을 입력하세요. 범위:R1~R50,S1~S50>");
            scanf(" %c%d", &mun, &seat);
           
            if (mun == 'R')
            {
              
                if((1<=seat)&&(seat<=50))
                {
                    
                    num2 = seat / 10;
                    res = seat % 10;
                  
                    if (rarr[num2][res-1]== 'x') {
                        printf("%c%d번 좌석은 이미 예약되어 있습니다.\n", mun, seat);
                        
                       
                    }
                    else if (rarr[num2 ][res-1] == 'o') {
                        printf("%c%d번 좌석은 이미 예약되어 있습니다\n", mun, seat);
                    }
                    else if (rarr[num2 ][res-1] == '_') {
                        printf("%c%d번 좌석이 예약되었습니다\n", mun, seat);
                        rarr[num2][res-1] = 'o';
                        sum += 50000;
                        
                    }
                }

                else {
                    printf("좌석 범위를 벗어났습니다.\n");
                }
            }
            else if (mun == 'S') {

                
                if ((1 <= seat) && (seat <= 50))
                {

                    num2 = seat / 10;
                    res = seat % 10;
            
                    if (sarr[num2][res - 1] == 'x') {
                        printf("%c%d번 좌석은 이미 예약되어 있습니다.\n", mun, seat);
                        

                    }
                    else if (sarr[num2 ][res - 1]== 'o') {
                        printf("%c%d번 좌석은 이미 예약되어 있습니다\n", mun, seat);
                    }
                    else if (sarr[num2 ][res - 1]== '_') {
                        printf("%c%d번 좌석이 예약되었습니다\n", mun, seat);
                        sarr[num2 ][res - 1] ='o';
                        sum +=30000;
                        
                    }
                }


                else {
                    printf("좌석 범위를 벗어났습니다.\n");
                }
            }



        }
        else if (num == 3) {
            printf("좌석을 입력하세요. 범위: R1~R50,S1~S50>");
            scanf(" %c%d",&mun, & seat);
            num2 = seat / 10;
            res = seat % 10;
            if (mun == 'R') {
                if ((1 <= seat) && (seat <= 50)) {
                    if (rarr[num2 ][res - 1] == 'o') {
                        printf("%c%d 번 좌석이 예약 취소되었습니다.\n", mun, seat);
                        sum -= 50000;
                        rarr[num2 ][res - 1] = "_";
                    }
                    else if (rarr[num2 ][res - 1] == 'x') {
                        printf("%c%d번 좌석은 귀하가 예약한 좌석이 아닙니다\n", mun, seat);
                    }
                    else if (rarr[num2 ][res - 1] == '_') {
                        printf("%c%d번 좌석은 예약된 좌석이 아닙니다\n", mun, seat);
                    }
                }
                else {
                    printf("좌석범위를 벗어났습니다\n");
                }

            }
            else if (mun == 'S') {
                if (sarr[num2 ][res-1] == 'o') {
                    printf("%c%d 번 좌석이 예약 취소되었습니다.\n", mun, seat);
                    sum -= 30000;
                    sarr[num2][res-1] = '_';
                }
                else if (sarr[num2 ][res-1] == 'x') {
                    printf("%c%d번 좌석은 귀하가 예약한 좌석이 아닙니다\n", mun, seat);
                }
                else if (sarr[num2][res-1] =='_') {
                    printf("%c%d번 좌석은 예약된 좌석이 아닙니다\n", mun, seat);
                }
                else {
                    printf("좌석범위를 벗어났습니다\n");
                }
            }
        }
        else {
            printf("예약된 좌석의 번호는 아래와 같습니다.\n");
            for (int i = 0;i < 5;i++) {
                for (int j = 0;j < 10;j++) {

                    if (rarr[i][j] == 'o'){
                        printf("R%d ", 10 * i + j + 1);
                    }
                }
            }
            for (int i = 0;i < 5;i++) {
                for (int j = 0;j < 10;j++) {

                    if (sarr[i][j] == 'o') {
                        printf("Sd%d ", 10 * i + j + 1);
                    }
                }
            }

            printf("\n");
            printf("총 결제 금액은 %d원입니다.\n", sum);
            break;
        }
    }
    return 0;
}