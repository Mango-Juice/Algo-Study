#include <stdio.h>
 
int main(void) {
    char input[102], output[202];
    char a, b, c;
    int idx = 0, odx = 0;

    scanf("%s %c %c %c", input, &a, &b, &c);

    while(input[idx] != '\0'){
        if(input[idx] == a || input[idx] == b || input[idx] == c){
            if(output[odx-1] != '\n') output[odx++] = '\n';
            output[odx++] = input[idx++];
            output[odx++] = '\n';
        }
        else{
            output[odx++] = input[idx++];
        }
    }

    printf("%s", output);
    
    return 0;
}
