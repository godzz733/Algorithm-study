#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;
vector<pair<int,int>> arr;
int N, K;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> N >> K;
	int bag[100001] = {};
	for (int i = 0; i < N; i++) {
		int a, b;
		cin >> a >> b;
		arr.push_back({a,b});
	}
	for (pair<int,int> curr: arr) {
		for (int i = K; i >= curr.first; i--) {
			bag[i] = max(bag[i - curr.first] + curr.second, bag[i]);
		}
	}
	cout << bag[K] << "\n";
	arr.clear();
	return 0;
}