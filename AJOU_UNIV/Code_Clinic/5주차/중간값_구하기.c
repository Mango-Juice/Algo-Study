#include <stdio.h>

int main(void){
    int a, b, c, tmp;
    scanf("%d %d %d", &a, &b, &c);

    if(b > a){
        tmp = b;
        b = a;
        a = tmp;
    }

    if(c > a) printf("%d", a);
    else if(c > b) printf("%d", c);
    else printf("%d", b);
    
    return 0;
}
