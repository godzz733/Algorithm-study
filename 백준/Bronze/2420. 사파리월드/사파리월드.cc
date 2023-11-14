#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
long long n, m;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> n >> m;
	cout << abs(n - m);
}