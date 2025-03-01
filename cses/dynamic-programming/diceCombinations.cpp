#include <bits/stdc++.h>
#define MOD 1'000'000'007
using namespace std;


int main() {
    int n; cin >> n;
    long long dp[n+1];
    dp[0] = 1; dp[1] = 1;
    for(int i = 2; i <= n; ++i) {
        dp[i] = 0;
        for(int j = 1; j <= 6; ++j) {
            if (i - j < 0) break;
            dp[i] += dp[i - j];
            dp[i] %= MOD;
        }
    }
    cout << dp[n] << endl;
}
