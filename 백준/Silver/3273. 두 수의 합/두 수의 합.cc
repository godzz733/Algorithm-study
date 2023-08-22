#include<iostream>
#include<string>
#include<cmath>
using namespace std;

int arr[2'000'001];
int n;
int a;
int x;
long ans = 0;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> a;
		arr[a]++;
	}
	cin >> x;
	for (int i = 1; i <= x/2; i++) {
		if (i == x - i) {
			ans += arr[i] * (arr[i] - 1) / 2;
		}
		else {
		ans += arr[i] * arr[x - i];
		}
	}
	cout << ans << '\n';
	
	
}