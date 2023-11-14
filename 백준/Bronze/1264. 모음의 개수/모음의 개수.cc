#include<iostream>
#include<algorithm>
#include<vector>
#include <string>
using namespace std;
string tem;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	while (1) {
		getline(cin, tem);
		transform(tem.begin(), tem.end(), tem.begin(), ::tolower);
		if (tem == "#") return 0;
		int ans = 0;
		for (int i = 0; i < tem.length(); i++) {
			if (tem[i] == 'a' || tem[i] == 'i' || tem[i] == 'u' || tem[i] == 'e' || tem[i] == 'o') ans++;
		}
		cout << ans << '\n';
	}
}