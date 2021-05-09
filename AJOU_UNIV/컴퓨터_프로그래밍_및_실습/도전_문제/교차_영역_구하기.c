#include <stdio.h>

void swap(int *x, int *y) {
	if(&x > &y){
		int tmp = *x;
		*x = *y;
		*y = tmp;
	}
}

int max(int a, int b){
	return a>b ? a : b;
}

int min(int a, int b){
	return a>b ? b : a;
}

int main() {
	int r1[4], r2[4];
	
	scanf("%d %d", &r1[0], &r1[2]);
	scanf("%d %d", &r1[1], &r1[3]);
	scanf("%d %d", &r2[0], &r2[2]);
	scanf("%d %d", &r2[1], &r2[3]);
	
	//편의를 위해 [xmin, xmax, ymin, ymax]의 순서로 바꿈.
	if(r1[0]>r1[1])swap(&r1[0],&r1[1]);
	if(r1[2]>r1[3])swap(&r1[2],&r1[3]);
	if(r2[0]>r2[1])swap(&r2[0],&r2[1]);
	if(r2[2]>r2[3])swap(&r2[2],&r2[3]);
	
	if(r1[1]<=r2[0] || r2[1]<=r1[0] 
		 || r1[3]<=r2[2] || r2[3]<=r1[2]) printf("0");
	else{
		printf("%d", 
					 (max(r1[0], r2[0]) - min(r1[1], r2[1])) 
					 * (max(r1[2], r2[2]) - min(r1[3], r2[3])));
	}
  return 0;
}
