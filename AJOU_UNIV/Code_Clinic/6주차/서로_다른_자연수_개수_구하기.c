#include <stdio.h>

int main(void){
    int s;
    int idx = 1, sum = 0;

    scanf("%d", &s);

    while(sum + idx <= s) sum += idx++;

    printf("%d", idx - 1);
    
    return 0;
}
