#include <stdio.h>

int main() {
	int n, m;
	int A[100000];
	int i, j;
	
	//N과 M을 첫 번째 줄에서 입력받는다 
	scanf("%d %d", &n, &m);
	
	//두 번째 줄에서 배열 A의 원소를 차례로 A[0]~A[n-1]에 입력받는다.
	for(i=0;i<n;i++)
	{
		scanf("%d", &A[i]);
	}
	
	//총 M개의 탐색할 숫자에 k대하여 
	for(i=0;i<m;i++)
	{
		int left = 0;
		int right = n-1;
		int mid;
		int k;
		int tmp = 0;
		
		//배열에서 찾을 숫자 k를 입력받는다.
		scanf("%d", &k);
		
		if(k < A[left] || k > A[right]){
			printf("NO\n");
			continue;
		}
		
		while(left <= right){
			mid = (left + right) / 2;
			if(A[mid] == k){
				printf("YES\n");
				tmp = 1;
				break;
			}
			else if(A[mid] > k) right = mid - 1;
			else left = mid + 1;
		}
		
		if(tmp == 0) printf("NO\n");
	}
	return 0;
}
