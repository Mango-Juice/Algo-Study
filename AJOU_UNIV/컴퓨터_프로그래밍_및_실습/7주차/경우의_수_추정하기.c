#include <stdio.h>
#define MAXIMUM 100000007

int main() {
	int n;
	unsigned long long last_white = 1;
	unsigned long long last_black_one = 1, last_black_two = 0;
	scanf("%d", &n);
	
	for(int i = 2; i <= n; i ++){
		unsigned long long tmp = last_black_one;
		last_black_one = last_white % MAXIMUM;
		last_white = (last_white + tmp + last_black_two) % MAXIMUM;
		last_black_two = tmp % MAXIMUM;
	}
	
	printf("%ld", (last_white + last_black_one + last_black_two) % MAXIMUM);
  return 0;
}
