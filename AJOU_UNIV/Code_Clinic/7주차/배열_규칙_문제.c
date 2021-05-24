#include <stdio.h>

int main(void){
    int idx = 1;
    int n;

    scanf("%d", &n);

    for(int i = 0; i < 5; i++){
        int j = 0;
        for(; j <= i; j++){
            if(idx % n == 0) printf("*%d* ", idx++);
            else printf("%d ", idx++);
        }
        for(; j < 5; j++) printf("0 ");
        printf("\n");
    }

    return 0; 
}
