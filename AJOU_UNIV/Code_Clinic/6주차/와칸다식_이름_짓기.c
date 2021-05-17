#include <stdio.h>
#include <string.h>

const char names[][5] = { "ka", "zu", "mi", "te", "ku", "lu", "ji", "ri", "ki", "zu", "me", "ta", "rin", "to", "mo", "no", "ke", "shi", "ari", "chi", "do", "ru", "mei", "na", "fu", "z" };
const char actors_w[][12] = { "T'Challa", "Killmonger", "Nakia", "Okoye", "Zuri", "W'Kabi", "Shuri" };
const char actors_r[][12] = { "chadwick", "micheal", "lupita", "danai", "forest", "Daniel", "letitia" };

int main(void) {
    //변수 선언
    char name[105];
    char answer[305];
    int idx = 0;

    //입력
    scanf("%s", name);

    //유명인인지 확인
    for (int i = 0; i < 7; i++) {
        if (strcmp(actors_r[i], name) == 0) {
            printf("%s", actors_w[i]);
            return 0;
        }
    }

    //유명인이 아니면
    while(name[idx] != '\0'){
        strcat(answer, names[(int) (name[idx++]) - 97]);
    }
    printf("%s", answer);
    return 0;
}
