#include <iostream>
#include <vector>
using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n;
	cin >> n;
	if (n == 0) {
		cout << 0;
		return 0;
	}
	else if (n == 1) {
		cout << 1;
		return 0;
	}

	long long* arr;
	arr = new long long[n + 1];
	for (int i = 0; i < n + 1; i++) {
		arr[i] = 0;
	}
	arr[1] = 1;
	for (int i = 2; i < n + 1; i++) {
		arr[i] = arr[i - 1] + arr[i - 2];
	}
	cout << arr[n] << "\n";

	
}