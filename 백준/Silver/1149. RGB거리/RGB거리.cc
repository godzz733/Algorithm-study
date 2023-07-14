#include <iostream>

using namespace std;
int n;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    int arr[1000][3];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 3; j++) {
            cin >> arr[i][j];
        }
    }
    int ans[1000][3];
    for (int i = 0; i < 3; i++) {
        ans[0][i] = arr[0][i];
    }

    for (int i = 1; i < n; i++) {
        for (int j = 0; j < 3; j++) {
            if (j == 0) {
                ans[i][j] = min(ans[i - 1][1] + arr[i][j], ans[i - 1][2] + arr[i][j]);
            }
            else if (j == 1) {
                ans[i][j] = min(ans[i - 1][0] + arr[i][j], ans[i - 1][2] + arr[i][j]);
            }
            else {
                ans[i][j] = min(ans[i - 1][0] + arr[i][j], ans[i - 1][1] + arr[i][j]);
            }
        }
    }
    cout << min(min(ans[n-1][0],ans[n-1][1]),ans[n-1][2]) << "\n";

}

