#include <stdio.h>
#include <stdlib.h>

int get_pivot_index(int arr[], int left, int right)
{
	return left; //pivot은 맨 왼쪽까
}

int arrange_array(int arr[], int left, int right, int pivot_index)
{
	int k = pivot_index;
	int low = left, high = right;
	int swap_target = right;

	while(low < high){
		while(low <= high && arr[low] <= arr[k]) low++;
		while(high >= low && arr[high] >= arr[k]) high--;
		if(low < high){
			int tmp = arr[low];
			arr[low] = arr[high];
			arr[high] = tmp;
		}
	}

	for(int i = left; i <= right; i++){
		if (arr[i] > arr[k]){
			swap_target = i;
			if(k < i) swap_target -= 1;
			break;
		}
	}
	
	int tmp = arr[swap_target];
	arr[swap_target] = arr[k];
	arr[k] = tmp;
	return swap_target;
}

void quick_sort(int arr[], int left, int right)
{
	int pivot_index;
	int k;
	
	if(left >= right) return;
	
	pivot_index = get_pivot_index(arr, left, right);
	k = arrange_array(arr, left, right, pivot_index);
	quick_sort(arr, left, k - 1);
	quick_sort(arr, k + 1, right);
}

int main()
{
	int n;
	int *arr;
	scanf("%d", &n);
	arr = (int*)malloc(sizeof(int) * n);
	
	for(int i = 0 ; i < n ; i ++)
	{
		scanf("%d", &arr[i]);
	}
	
	quick_sort(arr, 0, n-1);
	
	for(int i = 0 ; i < n ; i ++)
	{
		printf("%d\n", arr[i]);
	}
	
	free(arr);
	return 0;
}
