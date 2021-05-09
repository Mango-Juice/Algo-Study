#include <stdio.h>

int gcd(int a, int b)
{ 
    return (a % b == 0 ? b : gcd(b,a%b));
}

int main() {
	int a, b, result;
	scanf("%d %d", &a, &b);
	

	result = gcd(a, b);
	printf("%d\n%lld", result, (long long) result * (a/result) * (b/result));
  return 0;
}
