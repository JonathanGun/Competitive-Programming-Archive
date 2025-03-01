#include <bits/stdc++.h>
#define MOD 1'000'000'007
using namespace std;

int main() {
    int n, x; cin >> n >> x;
    int coins[n];
    for(int i = 0; i < n; ++i) {
        cin >> coins[i];
    }
    int dp[x+5];
    dp[0] = 1;
    for(int i = 1; i <= x; ++i) {
        dp[i] = 0;
        for(int j = 0; j < n; ++j) {
            if(i - coins[j] >= 0) {
                dp[i] += dp[i - coins[j]];
                dp[i] %= MOD;
            }
        }
    }
    cout << dp[x] << endl;
}