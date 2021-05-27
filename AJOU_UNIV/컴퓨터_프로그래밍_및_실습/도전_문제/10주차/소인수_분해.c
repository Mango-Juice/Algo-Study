#include <stdio.h>

void factorization(int n)
{
	for(int i = 2; i <= n; i ++){
		if(n % i == 0){
			printf("%d ", i);
			factorization(n / i);
			break;
		}
	}
}

int main()
{
	int n;
	scanf("%d", &n);
	
	factorization(n);
	
  return 0;
}
