import sys
input = sys.stdin.readline

cpu_max, pri_max = 1000, 500
n, cpu_target, ram_target = map(int, input().split())
arr = [[]] + [list(map(int, input().split())) for _ in range(n)]
dp = [[-float("inf")] * (cpu_max + 2) for _ in range(pri_max + 1)]
dp[0][0] = 0

answer = float('inf')
for i in range(1, n + 1):
    now_cpu, now_mem, now_pri = arr[i]
    for pri in range(pri_max, -1, -1):
        if pri + now_pri > pri_max:
            continue
        
        for cpu in range(cpu_max + 1, -1, -1):
            if cpu + now_cpu <= cpu_max: 
                dp[pri + now_pri][cpu + now_cpu] = max(dp[pri + now_pri][cpu + now_cpu], dp[pri][cpu] + now_mem)
                if cpu + now_cpu >= cpu_target and dp[pri + now_pri][cpu + now_cpu] >= ram_target:
                    answer = min(answer, pri + now_pri)
            else:
                dp[pri + now_pri][cpu_max + 1] = max(dp[pri + now_pri][cpu_max + 1], dp[pri][cpu] + now_mem)
                if cpu + now_cpu >= cpu_target and dp[pri + now_pri][cpu_max + 1] >= ram_target:
                    answer = min(answer, pri + now_pri)

print(answer if answer != float('inf') else -1)