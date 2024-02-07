// DP + 누적합
#include <stdio.h>

const int MOD = 1e9 + 7;

int i, t, a, b;
int answer, red, total, value;
int dp[501][50001];

int main(void) {
    // dp 미리 채우기
    dp[0][0] = 1;
    for (i = 1; i <= 500; ++i) {
        for (red = 0; red <= 50000; ++red) {
            if(red - i >= 0)
                dp[i][red] = (dp[i][red] + dp[i - 1][red - i]) % MOD;
            dp[i][red] = (dp[i][red] + dp[i - 1][red]) % MOD;
        }
    }
    
    // 누적합으로 변환
    for (i = 0; i <= 500; ++i) {
        for (red = 1; red <= 50000; ++red) {
            dp[i][red] = (dp[i][red] + dp[i][red - 1]) % MOD;
        }
    }
    
    // 입력
	scanf("%d", &t);

	while(t--){
		scanf("%d %d", &a, &b);
		answer = 0;

		for (i = 1; i <= 500; ++i) {
			total = i * (i + 1) / 2;
			
			if (total - b <= a) {
			    value = (dp[i][a] - (total - b > 0 ? dp[i][total - b - 1] : 0) + MOD) % MOD;
			    answer = (answer + value) % MOD;
			}
		}

		printf("%d\n", answer);
	}

	return 0;
}