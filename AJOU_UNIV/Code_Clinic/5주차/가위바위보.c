#include <stdio.h>

int main(void){
    const int rsp[4] = {0, 2, 3, 1};
    const int computer = 1;
    int user;
    scanf("%d", &user);

    if(user == computer) printf("무승부");
    else if(rsp[user] == computer) printf("패배");
    else printf("승리");
    
    return 0;
}
