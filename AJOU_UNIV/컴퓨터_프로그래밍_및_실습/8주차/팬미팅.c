#include <stdio.h>

int check(int arr[], int left, int right){
	for(int i = left + 1; i <= right; i++){
		for(int j = left; j < i; j++){
			if(arr[i] == arr[j]) return 0;
		}
	}
	return 1;
}

int main() {
	//변수 선언
	int n, k;
	int people[200002];
	int answer = 0, left = 0;
	
	//입력
	scanf("%d %d", &n, &k);
	for(int i = 0; i < n; i ++) scanf("%d", people + i);
	
	//작동
	if(k < 2){ printf("%d", n * k); return 0; } //예외 처리
	while(left <= n - k){
		if(check(people, left, left + k - 1)) answer += 1; 
		left++;
	}
	
	//출력
	printf("%d", answer);
	
  return 0;
}
