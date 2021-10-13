// https://codeforces.com/contest/1579/problem/E1

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <deque>

using namespace std;

int main() {
    int i, j, t, n;
    FAST_IO;

    cin >> t;

    for(i = 0; i < t; i++){
        deque<int> dq;
        cin >> n;

        for (j = 0; j < n; j++) {
            int tmp;
            cin >> tmp;

            if (dq.empty() || dq.front() > tmp) dq.push_front(tmp);
            else dq.push_back(tmp);
        }

        while(!dq.empty()) {
            cout << dq.front() << " ";
            dq.pop_front();
        }

        cout << '\n';

    }

    return 0;
}