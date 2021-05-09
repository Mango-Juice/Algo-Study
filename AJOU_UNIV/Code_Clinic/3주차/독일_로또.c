#include <stdio.h>

int nums[15];
int result[7];
int k;

void combi(int start, int depth){
    if(depth == 6){
        for(int i = 0; i < 6; i ++) printf("%d ", result[i]);
        printf("\n");
    }
    else{
        for(int i = start; i < k; i ++){
            result[depth] = nums[i];
            combi(i + 1, depth + 1);
        }
    }
}

int main(void) {
    scanf("%d ", &k);
    for(int i = 0; i < k; i ++) scanf("%d ", nums + i);
    combi(0, 0);
    
    return 0;
}
