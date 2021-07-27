// https://www.acmicpc.net/problem/1644

#include <iostream>
#include <vector>

using namespace std;

vector<int> v;

void setEra(int range) {
	bool *era = (bool*) malloc(sizeof(bool) * (range + 1));
	fill_n(era, range + 1, true);

	for (int i = 2; i <= range; i++) {
		if (!era[i]) continue;
		for (int j = i * 2; j <= range; j += i) era[j] = false;
	}

	for (int i = 2; i <= range; i++) {
		if (era[i]) v.push_back(i);
	}
	free(era);
}

int main(int argc, char** argv){
	int N, hap;
	int left = 0, right = 0, answer = 0;

	cin >> N;
	setEra(N);

	if (v.size() == 0) {
		cout << 0;
		return 0;
	}

	hap = v[0];

	while (left <= right && right < v.size()) {
		if (hap == N) {
			answer ++;
			hap -= v[left++];
			if(++right < v.size())hap += v[right];
		}
		else if (hap > N) hap -= v[left++];
		else if (++right < v.size())hap += v[right];
	}

	cout << answer;

	return 0;
}