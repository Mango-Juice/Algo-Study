#include <stdio.h>

int main(void){
    int m, d;
    int result = 0;
    int days[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    scanf("%d %d", &m, &d);

    while(m-->=1){
        result += d;
        d = days[m-1];
    }

    printf("%d", result%7);
}
