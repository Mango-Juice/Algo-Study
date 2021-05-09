#include <stdio.h>

int main(void){
    int rec1[4], rec2[4];

    for(int i = 0; i < 4;  i ++) scanf(" %d", rec1 + i);
    for(int i = 0; i < 4;  i ++) scanf(" %d", rec2 + i);

    if( rec1[0] < rec2[0] && rec1[1] < rec2[1]
        && rec1[0]+rec1[2] > rec2[0]  && rec1[1]+rec1[3] > rec2[1])
        printf("1");

    else if( rec1[0] > rec2[0] && rec1[1] > rec2[1]
        && rec1[0] < rec2[0]+rec2[2]  && rec1[1] < rec2[1]+rec2[3])
        printf("1");
    
    else
        printf("0");
    
}
