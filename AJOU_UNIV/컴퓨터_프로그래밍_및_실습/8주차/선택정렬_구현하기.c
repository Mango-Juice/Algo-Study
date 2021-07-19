#include <stdio.h>
#include <limits.h>

//arr[from] ~ arr[end]사이에서 가장 작은 숫자가 존재하는 칸의 인덱스를 반환하는 함수
int get_min_index(int arr[], int from, int end)
{
	int answer = 0;
	int minimum = INT_MAX;
	for(int i = from; i <= end; i ++){
		if(arr[i] < minimum) { answer = i; minimum = arr[i]; }
	}
	return answer;
}

//arr[0] ~ arr[size]를 정렬해주는 함수 
void sort(int arr[], int size)
{
	for(int i = 0; i < size - 1; i ++){
		int idx = get_min_index(arr, i, size - 1);
		int tmp = arr[i];
		arr[i] = arr[idx];
		arr[idx] = tmp;
	}
}

int main()
{
	int n;
	int i;
	int data[1000];
	
	scanf("%d", &n);
	for( i = 0 ; i < n ; i ++)
	{
		scanf("%d", &data[i]);
	}
	
	sort(data,n);
	
	for(i = 0 ; i < n ; i ++)
	{
		if(i > 0 )
			printf(" ");
		printf("%d", data[i]);
	}
	
  return 0;
}
