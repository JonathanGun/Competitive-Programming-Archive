#include <bits/stdc++.h>
#define MOD 1'000'000'007
using namespace std;

int main() {
    int n; cin >> n;
    long long dp[n+5][n+5];
    for(int i = 0; i <= n; ++i) dp[0][i] = 0;
    for(int i = 0; i <= n; ++i) dp[i][0] = 0;
    for(int i = 1; i <= n; ++i) {
        for(int j = 1; j <= n; ++j) {
            char c; cin >> c;
            dp[i][j] = c == '.';
        }
    }
    bool found = false;
    for(int i = 1; i <= n; ++i) {
        if (dp[1][i] == 0) found = true;
        if (found) dp[1][i] = 0;
    }
    found = false;
    for(int i = 1; i <= n; ++i) {
        if (dp[i][1] == 0) found = true;
        if (found) dp[i][1] = 0;
    }
    for(int i = 2; i <= n; ++i) {
        for(int j = 2; j <= n; ++j) {
            if(dp[i][j]) {
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
                dp[i][j] %= MOD;
            }
        }
    }
    // for(int i = 0; i <= n; ++i) {
    //     for(int j = 0; j <= n; ++j) {
    //         cout << dp[i][j] << " ";
    //     }cout << endl;
    // }cout << endl;
    cout << dp[n][n] << endl;
}