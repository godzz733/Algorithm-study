#include <iostream>
#include <vector>
using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n, m;
	cin >> n >> m;
	int * coin = new int[m+1];
	vector<int> arr;
	for (int i = 0; i < n; i++) {
		int tem;
		cin >> tem;
		arr.push_back(tem);
	}
	for (int i = 0; i < m+1; i++) {
		coin[i] = 987654321;
	}
	coin[m] = 0;
	for (int j = 0; j < n; j++) {
		for (int i = m; i >= arr[j]; i--) {
			coin[i - arr[j]] = min(coin[i - arr[j]], coin[i] + 1);
		}
	}
	int ans = coin[0] == 987654321 ? -1 : coin[0];
	cout << ans << "\n";

	
}