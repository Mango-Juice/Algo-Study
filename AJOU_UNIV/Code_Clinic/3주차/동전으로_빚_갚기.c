#include <stdio.h>

int main(void) {
    int n, k, a, b;
    scanf("%d %d", &n, &k);
    
    b = ceil((float)n / 400 - (float)k / 4);
    a = (n - 500 * b) / 100;

    printf("%d", a * 5 + b * 8);

    return 0;
}
