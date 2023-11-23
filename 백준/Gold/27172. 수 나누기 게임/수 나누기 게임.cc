#include<iostream>
#include<algorithm>
#include<unordered_set>
using namespace std;
int n;
int arr[100001];
int ans[1000001];
int tem;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	int *_max = max_element(begin(arr), end(arr));
	unordered_set<int> set(arr, arr + sizeof(arr)/sizeof(arr[0]));
	for (int i=0; i<n; i++){
		int x = arr[i];
		tem = x << 1;
		while (tem <= *_max) {
			if (set.find(tem) != set.end()) {
				ans[x]++;
				ans[tem]--;
			}
			tem += x;
		}
	}
	for (int i = 0; i < n; i++) {
		cout << ans[arr[i]] << " ";
	}
}