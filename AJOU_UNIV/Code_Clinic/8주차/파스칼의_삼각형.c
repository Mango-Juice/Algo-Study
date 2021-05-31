#include <stdio.h>

long long permutation(int n, int k){
    long long answer = 1;
    for(int i = n; i > n - k; i--) answer *= i;
    return answer;
}

int main(void){
    int n, k;
    scanf("%d %d", &n, &k);
    printf("%d", permutation(n - 1, k - 1) / permutation(k - 1, k - 1));
    return 0;
}
