#include <stdio.h>

int main(void){
    int a, b, c; 
    int idx = 0;
    char str[12]; 
    int count[10] = {0, };

    scanf(" %d %d %d", &a, &b, &c); //a, b, c 입력
    sprintf(str, "%d", a * b * c); //a, b, c의 곱을 str에 저장
    
    while(str[idx] != '\0') //str에서 한자리씩 검사
        count[(int) str[idx++] - 48] += 1; //해당되는 숫자의 갯수 += 1
    
    for(int i=0; i<10; i++){ //출력
        if(i != 0) printf(" ");
        printf("%d", count[i]);
    }
}
