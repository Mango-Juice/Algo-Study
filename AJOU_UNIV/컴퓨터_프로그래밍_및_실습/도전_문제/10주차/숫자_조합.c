#include <stdio.h>

void choice(int n, int k, int cnt, int numbers[])
{
	if (cnt > k)
	{	
		for (int i = 1; i <= k ;i++)
		{
			if (i >= 2)
			{
				printf("-");
			}
			printf("%d", numbers[i]);
		}
		printf("\n");

		return;
	}

	for(int i = numbers[cnt - 1] + 1; i <= n; i++){
		numbers[cnt] = i;
		choice(n, k, cnt + 1, numbers);
	} 
}

int main() {
	int n, k;
	int *numbers;

	scanf("%d %d", &n, &k);
	numbers = (int*)malloc(sizeof(int) * (k + 1));
	numbers[0] = 0;

	choice(n, k, 1, numbers);

	free(numbers);

	return 0;
}
