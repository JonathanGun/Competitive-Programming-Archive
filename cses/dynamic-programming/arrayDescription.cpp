#include <bits/stdc++.h>
#define MOD 1'000'000'007
using namespace std;

int main() {
    int n, m; cin >> n >> m;
    int arr[n];
    for(int i = 0; i < n; ++i) {
        cin >> arr[i];
    }
    int dp[n + 1][m + 1];
    for(int i = 0; i <= n; ++i) {
        for(int j = 0; j <= m; ++j) {
            dp[i][j] = 0;
        }
    }
    int first = arr[0];
    if (first == 0) {
        for(int j = 1; j <= m; ++j) {
            dp[1][j] = 1;
        }
    } else {
        dp[1][arr[0]] = 1;
    }
    for(int i = 2; i <= n; ++i) {
        int cur = arr[i - 1];
        if (cur == 0) {
            for(int j = 1; j <= m; ++j) {
                dp[i][j] += dp[i-1][j];
                if (j - 1 >= 1) {
                    dp[i][j] += dp[i-1][j-1];
                    dp[i][j] %= MOD;
                }
                if (j + 1 <= m) {
                    dp[i][j] += dp[i-1][j+1];
                    dp[i][j] %= MOD;
                }
            }
        } else {
            dp[i][cur] = dp[i-1][cur];
            if (cur - 1 >= 1) {
                dp[i][cur] += dp[i-1][cur-1];
                dp[i][cur] %= MOD;
            }
            if (cur + 1 <= m) {
                dp[i][cur] += dp[i-1][cur+1];
                dp[i][cur] %= MOD;
            }
        }
    }
    // for(int i = 0; i <= n; ++i) {
    //     for(int j = 0; j <= m; ++j) {
    //         cout << dp[i][j] << " ";
    //     }cout << endl;
    // }cout << endl;
    long long ans = 0;
    for(int j = 1; j <= m; ++j) {
        ans += dp[n][j];
        ans %= MOD;
    }
    cout << ans << endl;
    // cout << dp[n][m] << endl;
}