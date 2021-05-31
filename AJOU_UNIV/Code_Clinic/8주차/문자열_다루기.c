#include <stdio.h>
#include <string.h>
#include <stdlib.h>


// 문자열의 순서를 뒤집어 리턴하는 함수
char* reverse(char *string){
    char *answer = malloc(sizeof(char) * 100);
    int length = strlen(string);

    for(int i = 0; i < length; i ++) answer[length - i - 1] = string[i];

    return answer;
}

// 문자열에서 자음의 수를 리턴하는 함수
int count_c(char* string){
    int answer = 0;
    int idx = 0;

    while(string[idx] != '\0'){
        char c = string[idx++];
        if(c > 90) c -= 32;
        if(c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') continue;
        if( c >= 65 && c <= 90) answer += 1;
    }
    return answer;
}

// 문자열에서 모음의 수를 리턴하는 함수
int count_v(char* string){
    int answer = 0;
    int idx = 0;

    while(string[idx] != '\0'){
        char c = string[idx++];
        if(c > 90) c -= 32;
        if(c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') answer += 1;
    }
    return answer;
}

// 문자열의 대소문자를 바꾸어 리턴하는 함수
char* updown(char *string){
    char *answer = malloc(sizeof(char) * 100);
    int idx = 0;

    while(string[idx] != '\0'){
        char c = string[idx];
        if(c >= 65 && c <= 90) c += 32;
        else if(c >= 97 && c <= 122) c -= 32;
        answer[idx++] = c;
    }

    return answer;
}


// 메인 함수
int main(void){
    char str[100];
    char tmp[100];

    while(gets(tmp)){
        strcat(str, tmp);
        strcat(str, " ");
    }

    printf("%s %d %d %s", reverse(str), count_c(str), count_v(str), updown(str));
    return 0;
}
