#include <stdio.h>
#include <math.h>

int sum(int n){
    int result = 0;
    for(int i = 1; i <= n; i++) result += i;
    return result;
}

int main(void) {
    int n;
    int is_positive;

    scanf("%d", &n);
    is_positive = n < 0 ? -1 : 1;

    printf("%d", sum(abs(n)) * is_positive);
    return 0;
}
