#include <bits/stdc++.h>
#define MOD 1'000'000'007
using namespace std;

int main() {
    int n, x; cin >> n >> x;
    int prices[n], pages[n];
    for(int i = 0; i < n; ++i) cin >> prices[i];
    for(int i = 0; i < n; ++i) cin >> pages[i];
    
    int dp[n + 5][x + 5];
    for(int i = 0; i <= n; ++i) dp[i][0] = 0;
    for(int j = 0; j <= x; ++j) dp[0][j] = 0;
    for(int i = 1; i <= n; ++i) {
        for(int j = 1; j <= x; ++j) {
            dp[i][j] = dp[i-1][j];
            if (prices[i-1] <= j) {
                dp[i][j] = max(dp[i][j], dp[i-1][j-prices[i - 1]] + pages[i-1]);
            }
        }
    }
    // for(int i = 0; i <= n; ++i) {
    //     for(int j = 0; j <= x; ++j) {
    //         cout << dp[i][j] << " ";
    //     }cout << endl;
    // }cout << endl;
    cout << dp[n][x] << endl;
}

