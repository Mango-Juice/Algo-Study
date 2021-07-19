#K 경유지 내 가장 저렴한 항공권
#https://leetcode.com/problems/cheapest-flights-within-k-stops

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        inp = {}
        self.answer = 10000000
        
        def dfs(from_: int, distance: int, cost: int, visited: List[int] = []) -> None:
            if distance > k + 1 or self.answer < cost or from_ in visited: #이미 최저가보다 비싸거나 경유지 제한을 넘겼거나 다시 되돌아 왔다면
                return # 리턴
            if from_ == dst: #목적지에 도착했다면
                self.answer = cost #가격 저장
                
            if from_ in inp:
                for t, p in inp[from_]:
                    dfs(t, distance + 1, cost + p, visited + [from_])
        
        for f, t, p in flights:
            if f in inp.keys():
                inp[f].append((t, p))
            else:
                inp[f] = [(t, p)]
                
        dfs(src, 0, 0)
        
        return self.answer if not self.answer == 10000000 else -1
