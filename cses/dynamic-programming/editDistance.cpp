#include <bits/stdc++.h>
#define MOD 1'000'000'007
using namespace std;

int main() {
    string s, t;
    cin >> s >> t;
    int n = s.length(), m = t.length();
    long long dp[n + 1][m + 1];
    for(int i = 0; i <= n; ++i) {
        for(int j = 0; j <= m; ++j) {
            if (i == 0) dp[i][j] = j;
            else if (j == 0) dp[i][j] = i;
            else if (s[i-1] == t[j-1]) dp[i][j] = dp[i-1][j-1];
            else {
                dp[i][j] = min(min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]) + 1;
            }
        }
    }
    // for(int i = 0; i <= n; ++i) {
    //     for(int j = 0; j <= m; ++j) {
    //         cout << dp[i][j] << " ";
    //     }cout << endl;
    // }cout << endl;
    cout << dp[n][m] << endl;
}