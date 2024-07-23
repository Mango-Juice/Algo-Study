#include <bits/stdc++.h>

#define F first
#define S second
#define B begin()
#define E end()
#define PB push_back
#define MP make_pair
#define REP(i, a, b) for (int i = a; i < b; i++)
#define endl "\n"

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    
    int n, m, a, b, c;
    int dist[201][201];
    int way[201][201] = {0, };
    
    cin >> n >> m;
    
    REP(i, 0, n) REP(j, 0, n) dist[i][j] = 200001;
    
    REP(i, 0, m) {
        cin >> a >> b >> c;
        a--; b--;
        dist[a][b] = c; dist[b][a] = c;
        way[a][b] = b; way[b][a] = a;
    }
    
    REP(k, 0, n) {
        REP(i, 0, n) {
            REP(j, 0, n) {
                if (i == j) continue;
                if (dist[i][j] > dist[i][k] + dist[k][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                    way[i][j] = way[i][k];
                }
            }
        }
    }
    
    REP(i, 0, n) {
        REP(j, 0, n) {
            if (i == j) cout << "-";
            else cout << way[i][j] + 1;
            cout << " ";
        }
        cout << endl;
    }
}