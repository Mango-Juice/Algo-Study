// https://www.acmicpc.net/problem/4781

#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

int weight[5001];
int price[5001];
int dp[100001];
int n, im;

int solution(int money)
{
    int& result = dp[money];

    if (result > -1) return result;

    result = 0;

    for (int i = 0; i < n; i++)
        if (money >= price[i])
            result = max(result, weight[i] + solution(money - price[i]));

    return result;
}

int main()
{
    double m, p;

    while (true) {
        memset(dp, -1, sizeof(dp));
        scanf(" %d %lf", &n, &m);
        im = (int)(m * 100 + 0.5);

        if (n == 0 && im == 0) break;

        for (int i = 0; i < n; i++) {
            scanf(" %d %lf", &weight[i], &p);
            price[i] = (int)(p * 100 + 0.5);
        }

        printf("%d\n", solution(im));

    }
    
    return 0;
}