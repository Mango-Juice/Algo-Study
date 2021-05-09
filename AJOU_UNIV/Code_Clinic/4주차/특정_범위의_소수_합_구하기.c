#include <stdio.h>

int main(void) {
	//변수 선언
	int n;
	int sosu[1001] = {0, };
	int count = 0, sum = 0;

	//에라토스테네스의 체
	sosu[0] = 1, sosu[1] = 1;
	for(int i = 2; i <= 500; i++){
		if(sosu[i] == 1) continue;
		for(int j = 2; i * j <= 1000; j++){
			sosu[ i * j ] = 1;
		} 
	}

	//입력
	scanf("%d", &n);
	
	//출력
	for(int i = n; i <= 1000; i ++){
		if(sosu[ i ] == 0){
			printf("%d ", i);
			count ++;
			sum += i;
		}
	}
	printf("%d %d", count, sum);
}
